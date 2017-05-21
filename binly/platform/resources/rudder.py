import logging
from os.path import (dirname, abspath, join)
import sys
from binly.utils.resource import Resource


class Rudder(Resource):
    SERVO_MIN = 204  # Min pulse length out of 4096.
    SERVO_MAX = 410  # Max pulse length out of 4096.
    SERVO_CHANNEL = 0
    SERVO_PWM_FREQ_HZ = 50
    RUDDER_KEY = 'rudder'
    MIN_RUDDER = -5
    MAX_RUDDER = 5

    def __init__(self, fake=False, *vargs, **kwargs):
        super(Rudder, self).__init__(*vargs, **kwargs)
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
        logging.debug('Received RUDDER message on topic "%s": %s' %
                      (topic, data))

        # Ensure the rudder value is given in the data.
        if self.RUDDER_KEY not in data:
            logging.info('Rudder data does not contain %s key' %
                         self.RUDDER_KEY)
            return
        # Validate the requested rudder value.
        rudder = self.validate_value(
            'Rudder',
            data[self.RUDDER_KEY], self.MIN_RUDDER, self.MAX_RUDDER)

        # Reverse the rudder value because the servo is backwards.
        rudder = -rudder

        # Make the servo move.
        self._pwm.set_pwm(self.SERVO_CHANNEL, 0, self.scale_value(
            rudder, self.MIN_RUDDER, self.MAX_RUDDER, self.SERVO_MIN,
            self.SERVO_MAX))

    @staticmethod
    def validate_rudder(rudder, min_rudder, max_rudder):
        """ Validate the rudder value is between min_rudder and max_rudder. """
        if rudder < min_rudder:
            logging.warning('Rudder value %d less than minimum value of %d. \
Setting to minimum.' % (rudder, min_rudder))
            rudder = min_rudder
        if rudder > max_rudder:
            logging.warning('Rudder value %d greater than maximum value of \
%d. Setting to maximum.' % (rudder, max_rudder))
            rudder = max_rudder
        return rudder


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
