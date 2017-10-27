import logging
from os.path import (dirname, abspath, join)
import sys
from binly.utils.resource import Resource


class Servo(Resource):
    DEFAULT_SERVO_MIN = 90  # Min pulse length out of 4096.
    DEFAULT_SERVO_MAX = 545  # Max pulse length out of 4096.
    SERVO_PWM_FREQ_HZ = 50

# TODO adjust arm servo ranges.

    def __init__(self, name, servo_channel, min_value, max_value,
                 servo_min=DEFAULT_SERVO_MIN, servo_max=DEFAULT_SERVO_MAX,
                 fake=False, *vargs, **kwargs):
        super(Servo, self).__init__(*vargs, **kwargs)
        self.name = name
        self.servo_channel = servo_channel
        self.min_value = min_value
        self.max_value = max_value
        self.servo_min = servo_min
        self.servo_max = servo_max
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
        scaled_value = self.scale_value(
            new_value, self.min_value, self.max_value,
            self.servo_min, self.servo_max)
        logging.debug('Setting servo value to: %s' % (scaled_value))
        self._pwm.set_pwm(self.servo_channel, 0, scaled_value)


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
