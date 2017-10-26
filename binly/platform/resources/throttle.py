import atexit
import logging
from os.path import (dirname, abspath, join)
import sys
from binly.utils.resource import Resource

# TODO Turn Throttle into a motor set controller.


class Throttle(Resource):
    MOTOR_HAT_ADDRESS = 0x61
    MOTOR_LEFT_FRONT = 1
    MOTOR_LEFT_REAR = 2
    MOTOR_RIGHT_FRONT = 3
    MOTOR_RIGHT_REAR = 4
    MIN_THROTTLE_FOR_SCALE = 0
    MIN_THROTTLE = -5
    MAX_THROTTLE = 5
    MOTOR_MIN = 0
    MOTOR_MAX = 250

    def __init__(self, fake=False, *vargs, **kwargs):
        super(Throttle, self).__init__(*vargs, **kwargs)
        self.throttle = 0
        self.steering = 0
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
        self._left_front_motor = self._motor_hat.getMotor(
            self.MOTOR_LEFT_FRONT)
        self._left_rear_motor = self._motor_hat.getMotor(
            self.MOTOR_LEFT_REAR)
        self._right_front_motor = self._motor_hat.getMotor(
            self.MOTOR_RIGHT_FRONT)
        self._right_rear_motor = self._motor_hat.getMotor(
            self.MOTOR_RIGHT_REAR)

        def turn_off_motors():
            self.set_motor_run(self._motor_commands.RELEASE)

        atexit.register(turn_off_motors)

    def start(self):
        self.start_processing_incoming_messages()

    def handle_incoming_message(self, topic, value):
        logging.debug('Received throttle message on topic "%s": %s' %
                      (topic, value))

        if topic == 'throttle':
            # Validate and update with the requested throttle value.
            self.throttle = self.validate_value(
                'Throttle',
                value, self.MIN_THROTTLE, self.MAX_THROTTLE)

        elif topic == 'scaled-steering':
            self.steering = value

        # Update the motors based on the current settings.
        self.update_motor_state()

    def update_motor_state(self):
        # Determine motor direction based on throttle sign.
        # Determine max motor speed based on throttle magnitude.
        if self.throttle > 0:
            self.set_motor_run(self._motor_commands.FORWARD)
            speed = self.scale_speed(self.throttle)
        elif self.throttle < 0:
            self.set_motor_run(self._motor_commands.BACKWARD)
            speed = self.scale_speed(-self.throttle)
        else:
            self.set_motor_run(self._motor_commands.BRAKE)
            self.set_motor_speed(0)
            return

        # Determine which side to scale down based on steering sign.
        if self.steering < 0:
            self.set_left_motor_speed(int(speed * -self.steering))
            self.set_right_motor_speed(speed)
        else:
            self.set_left_motor_speed(speed)
            self.set_right_motor_speed(int(speed * self.steering))

    def set_motor_run(self, motor_command):
        self._left_front_motor.run(motor_command)
        self._left_rear_motor.run(motor_command)
        self._right_front_motor.run(motor_command)
        self._right_rear_motor.run(motor_command)

    def set_motor_speed(self, speed):
        self.set_left_motor_speed(speed)
        self.set_right_motor_speed(speed)

    def set_left_motor_speed(self, speed):
        self._left_front_motor.setSpeed(speed)
        self._left_rear_motor.setSpeed(speed)

    def set_right_motor_speed(self, speed):
        self._right_front_motor.setSpeed(speed)
        self._right_rear_motor.setSpeed(speed)

    def scale_speed(self, speed):
        return self.scale_value(
            speed, self.MIN_THROTTLE_FOR_SCALE, self.MAX_THROTTLE,
            self.MOTOR_MIN, self.MOTOR_MAX)


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
