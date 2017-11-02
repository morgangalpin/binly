import logging
from os.path import (dirname, abspath, join)
import math
import numpy
import sys
import time
from binly.utils.resource import Resource


class Servo(Resource):
    # Min pulse length out of 4096.
    DEFAULT_SERVO_MIN = 90

    # Max pulse length out of 4096.
    DEFAULT_SERVO_MAX = 545

    # Max number of servo units to change per time unit.
    DEFAULT_MAX_SERVO_RATE = 25

    # Number of seconds between servo movement updates.
    SERVO_UPDATE_SLEEP_SECONDS = 1.0 / 10.0

    # Servo pulse width modulation frequency in Hertz.
    SERVO_PWM_FREQ_HZ = 50

    def __init__(self, name, servo_channel, min_value, max_value,
                 initial_value, servo_min=DEFAULT_SERVO_MIN,
                 servo_max=DEFAULT_SERVO_MAX,
                 max_servo_rate=DEFAULT_MAX_SERVO_RATE,
                 fake=False, *vargs, **kwargs):
        super(Servo, self).__init__(*vargs, **kwargs)
        self.name = name
        self.servo_channel = servo_channel
        self.min_value = min_value
        self.max_value = max_value
        self.servo_min = servo_min
        self.servo_max = servo_max
        self.max_servo_rate = max_servo_rate
        if fake:
            self._pwm = FakePCA9685(self.name)
        else:
            path = join(dirname(dirname(dirname(dirname(
                abspath(__file__))))),
                'submodules', 'Adafruit_Python_PCA9685')
            if path not in sys.path:
                sys.path.append(path)
            import Adafruit_PCA9685
            self._pwm = Adafruit_PCA9685.PCA9685()
            self._pwm.set_pwm_freq(self.SERVO_PWM_FREQ_HZ)

        # Initialize the servo to the initial value.
        self.servo_value = self.scale_value(
            initial_value, self.min_value, self.max_value,
            self.servo_min, self.servo_max)
        logging.debug('Setting servo value to initial value: %s'
                      % (self.servo_value))
        self._pwm.set_pwm(self.servo_channel, 0, self.servo_value)

    def start(self):
        self.start_processing_incoming_messages()

    def handle_incoming_message(self, topic, value):
        logging.debug('Received %s message on topic "%s": %s' %
                      (self.name, topic, value))

        # Validate the requested value.
        new_value = self.validate_value(
            self.name,
            value, self.min_value, self.max_value)

        # Make the servo move.
        new_servo_value = self.scale_value(
            new_value, self.min_value, self.max_value,
            self.servo_min, self.servo_max)
        for servo_value in self.smooth_value_series(self.servo_value,
                                                    new_servo_value,
                                                    self.max_servo_rate):
            logging.debug('Setting servo value to: %s' % (servo_value))
            self._pwm.set_pwm(self.servo_channel, 0, servo_value)
            time.sleep(self.SERVO_UPDATE_SLEEP_SECONDS)
        self.servo_value = new_servo_value

    @staticmethod
    def smooth_value_series(start_value, end_value, max_rate):
        num_samples = int(
            math.ceil(abs(float(start_value - end_value)) / max_rate)) + 1
        return numpy.linspace(start_value, end_value, num_samples)
        # if length <= 1:
        #     return [end_value]
        # step_size = float(start_value - end_value) / (length - 1)
        # result = []

        # return result

    #     # create function for doing interpolation of the desired
    #     # ranges
    #     scaler = make_interpolater(1, 512, 5, 10)

    #     # receive list of raw values from sensor, assign to data_list

    #     # now convert to scaled values using map
    #     scaled_data = map(scaler, data_list)

    #     # or a list comprehension, if you prefer
    #     scaled_data = [scaler(x) for x in data_list]

    # def make_interpolater(left_min, left_max, right_min, right_max):
    #     # Figure out how 'wide' each range is
    #     leftSpan = left_max - left_min
    #     rightSpan = right_max - right_min

    #     # Compute the scale factor between left and right values
    #     scaleFactor = float(rightSpan) / float(leftSpan)

    #     # create interpolation function using pre-calculated scaleFactor
    #     def interp_fn(value):
    #         return right_min + (value - left_min) * scaleFactor

    #     return interp_fn


class FakePCA9685(object):
    """ Implements the same interface as the Adafruit_PCA9685.PCA9685, but
    none of the methods do anything.
    """

    def __init__(self, name, *vargs, **kwargs):
        super(FakePCA9685, self).__init__(*vargs, **kwargs)
        self.name = name

    def set_pwm_freq(self, freq_hz):
        logging.debug('%s: FakePCA9685.set_pwm_freq(%d)' %
                      (self.name, freq_hz))

    def set_pwm(self, channel, on, off):
        logging.debug('%s: FakePCA9685.set_pwm(%d, %d, %d)' %
                      (self.name, channel, on, off))

    def set_all_pwm(self, on, off):
        logging.debug('%s: FakePCA9685.set_all_pwm(%d, %d)' %
                      (self.name, on, off))
