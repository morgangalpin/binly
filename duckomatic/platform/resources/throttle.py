import atexit
import logging
from os.path import (dirname, abspath, join)
import sys
from duckomatic.utils.resource import Resource


class Throttle(Resource):
    MOTOR_HAT_ADDRESS = 0x61
    MOTOR_NUM = 1
    THROTTLE_KEY = 'throttle'
    MIN_THROTTLE = 0
    MAX_THROTTLE = 10
    MOTOR_MIN = 0
    MOTOR_MAX = 255

    def __init__(self, fake=False, *vargs, **kwargs):
        super(Throttle, self).__init__(*vargs, **kwargs)
        if fake:
            self._motor_hat = FakeMotorHat()
            self._motor_commands = DcMotorCommands()
        else:
            sys.path.append(join(dirname(dirname(dirname(dirname(
                abspath(__file__))))),
                'submodules', 'Adafruit-Motor-HAT-Python-Library'))
            import Adafruit_MotorHAT
            self._motor_hat = Adafruit_MotorHAT.Adafruit_MotorHAT(
                addr=self.MOTOR_HAT_ADDRESS)
            self._motor_commands = DcMotorCommands(
                adafruit_motor_hat=self._motor_hat)
        self._motor = self._motor_hat.getMotor(self.MOTOR_NUM)

        def turn_off_motors():
            self._motor_hat.getMotor(1).run(self._motor_commands.RELEASE)
            self._motor_hat.getMotor(2).run(self._motor_commands.RELEASE)
            self._motor_hat.getMotor(3).run(self._motor_commands.RELEASE)
            self._motor_hat.getMotor(4).run(self._motor_commands.RELEASE)

        atexit.register(turn_off_motors)

    def start(self):
        self._motor.run(self._motor_commands.FORWARD)
        self.start_processing_incoming_messages()

    def handle_incoming_message(self, topic, data):
        logging.debug('Received THROTTLE message on topic "%s": %s' %
                      (topic, data))

        # Ensure the throttle value is given in the data.
        if self.THROTTLE_KEY not in data:
            logging.warning('Throttle data does not contain %s key' %
                            self.THROTTLE_KEY)
            return
        # Validate the requested throttle value.
        throttle = self.validate_value(
            'Throttle',
            data[self.THROTTLE_KEY], self.MIN_THROTTLE, self.MAX_THROTTLE)

        # Change the motor speed.
        self._motor.setSpeed(self.scale_value(
            throttle, self.MIN_THROTTLE, self.MAX_THROTTLE,
            self.MOTOR_MIN, self.MOTOR_MAX))


class FakeMotorHat(object):
    """ Implements the same interface as the
    Adafruit_MotorHAT.Adafruit_MotorHAT, but none of the methods do anything.
    """

    def __init__(self, *vargs, **kwargs):
        super(FakeMotorHat, self).__init__(*vargs, **kwargs)

    def setPin(self, pin, value):
        logging.debug('FakeMotorHat.setPin(%d, %d)' % (pin, value))

    def getStepper(self, steps, num):
        logging.debug('FakeMotorHat.getStepper(%d, %d)' % (steps, num))

    def getMotor(self, num):
        logging.debug('FakeMotorHat.getMotor(%d)' % (num))
        return FakeDcMotor()


class FakeDcMotor(object):
    """ Implements the same interface as the
    Adafruit_MotorHAT.Adafruit_DCMotor, but none of the methods do anything.
    """

    def __init__(self, *vargs, **kwargs):
        super(FakeDcMotor, self).__init__(*vargs, **kwargs)

    def run(self, command):
        logging.debug('FakeDcMotor.run(%d)' % (command))

    def setSpeed(self, speed):
        logging.debug('FakeDcMotor.setSpeed(%d)' % (speed))


class DcMotorCommands(object):
    """ Holds the command values to send to DC motors. """
    FORWARD = 1
    BACKWARD = 2
    BRAKE = 3
    RELEASE = 4

    def __init__(self, adafruit_motor_hat=None, *vargs, **kwargs):
        super(DcMotorCommands, self).__init__(*vargs, **kwargs)
        if adafruit_motor_hat is not None:
            self.FORWARD = adafruit_motor_hat.FORWARD
            self.BACKWARD = adafruit_motor_hat.BACKWARD
            self.BRAKE = adafruit_motor_hat.BRAKE
            self.RELEASE = adafruit_motor_hat.RELEASE
