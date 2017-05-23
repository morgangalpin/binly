import logging
from os.path import (dirname, abspath, join)
import sys
from binly.utils.resource import Resource


class Steering(Resource):
    SERVO_MIN = 204  # Min pulse length out of 4096.
    SERVO_MAX = 410  # Max pulse length out of 4096.
    SERVO_CHANNEL = 0
    SERVO_PWM_FREQ_HZ = 50
    DATA_KEY = 'steering'
    MIN_VALUE = -5
    MAX_VALUE = 5

    def __init__(self, fake=False, *vargs, **kwargs):
        super(Steering, self).__init__(*vargs, **kwargs)
        if fake:
            self._pwm = FakePCA9685()
        else:
            sys.path.append(join(dirname(dirname(dirname(dirname(
                abspath(__file__))))),
                'submodules', 'Adafruit_Python_PCA9685'))
            import Adafruit_PCA9685
            self._pwm = Adafruit_PCA9685.PCA9685()
            self._pwm.set_pwm_freq(self.SERVO_PWM_FREQ_HZ)

    def start(self):
        self.start_processing_incoming_messages()

    def handle_incoming_message(self, topic, data):
        logging.debug('Received Steering message on topic "%s": %s' %
                      (topic, data))

        # Ensure the steering value is given in the data.
        if self.DATA_KEY not in data:
            logging.info('Steering data does not contain %s key' %
                         self.DATA_KEY)
            return
        # Validate the requested steering value.
        steering = self.validate_value(
            'Steering',
            data[self.DATA_KEY], self.MIN_VALUE, self.MAX_VALUE)

        # Reverse the steering value because the servo is backwards.
        steering = -steering

        # Make the servo move.
        self._pwm.set_pwm(self.SERVO_CHANNEL, 0, self.scale_value(
            steering, self.MIN_VALUE, self.MAX_VALUE, self.SERVO_MIN,
            self.SERVO_MAX))

    @staticmethod
    def validate_steering(steering, min_steering, max_steering):
        """ Validate the steering value is between min_steering and max_steering. """
        if steering < min_steering:
            logging.warning('Steering value %d less than minimum value of %d. \
Setting to minimum.' % (steering, min_steering))
            steering = min_steering
        if steering > max_steering:
            logging.warning('Steering value %d greater than maximum value of \
%d. Setting to maximum.' % (steering, max_steering))
            steering = max_steering
        return steering


class FakePCA9685(object):
    """ Implements the same interface as the Adafruit_PCA9685.PCA9685, but
    none of the methods do anything.
    """

    def __init__(self, *vargs, **kwargs):
        super(FakePCA9685, self).__init__(*vargs, **kwargs)

    def set_pwm_freq(self, freq_hz):
        logging.debug('FakePCA9685.set_pwm_freq(%d)' % (freq_hz))

    def set_pwm(self, channel, on, off):
        logging.debug('FakePCA9685.set_pwm(%d, %d, %d)' % (channel, on, off))

    def set_all_pwm(self, on, off):
        logging.debug('FakePCA9685.set_all_pwm(%d, %d)' % (on, off))
