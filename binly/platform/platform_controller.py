# import logging
import threading

from binly.platform.resources.camera import Camera
from binly.platform.resources.gps import Gps
from binly.platform.resources.steering import Steering
from binly.platform.resources.throttle import Throttle
from binly.platform.resources.servo import Servo


class PlatformController(object):
    """ Main controller for the robot platform.
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self,
                 camera1_image_dir,
                 camera_image_format='%d.jpg',
                 camera1_image_max_age_seconds=60,
                 fake=False):
        """ Constructor.
        Creates a thread and starts it immediately.

        @param fake True to fake the integration to the actual Pi hardware.
        Defaults to false which means to actually interact with the servos
        and motors and whatnot.
        """
        super(PlatformController, self).__init__()
        self.fake = fake

        self._resources = {}
        self._thread = None
        self._stop = threading.Event()
        self._stop.set()

        self.add_resource('camera', Camera(
            fake=self.fake, image_dir=camera1_image_dir,
            image_format=camera_image_format,
            max_image_age_seconds=camera1_image_max_age_seconds))
        self.add_resource('gps', Gps())
        steering = Steering()
        self.add_resource('steering', steering)
        self.add_resource('throttle', Throttle(fake=self.fake))
        self.add_resource_subscriber_to_publisher(
            'throttle', steering.get_publisher(), 'scaled-steering')

        self.add_resource('gripper', Servo(
            name='Gripper', servo_channel=0, min_value=0, max_value=200,
            servo_min=175, servo_max=395, fake=self.fake))
        self.add_resource('wrist-rotate', Servo(
            name='WristRotate', servo_channel=1, min_value=-100, max_value=100,
            servo_min=110, servo_max=545, fake=self.fake))
        self.add_resource('wrist-bend', Servo(
            name='WristBend', servo_channel=2, min_value=-100, max_value=100,
            servo_min=120, servo_max=390, fake=self.fake))
        self.add_resource('elbow-bend', Servo(
            name='ElbowBend', servo_channel=3, min_value=-100, max_value=100,
            servo_min=90, servo_max=545, fake=self.fake))
        self.add_resource('shoulder-bend', Servo(
            name='ShoulderBend', servo_channel=4, min_value=-100, max_value=100,
            servo_min=100, servo_max=515, fake=self.fake))
        self.add_resource('shoulder-rotate', Servo(
            name='ShoulderRotate', servo_channel=5, min_value=-100,
            max_value=100, servo_min=90, servo_max=545, fake=self.fake))

    def start(self):
        for _, resource in self._resources.items():
            resource.start()

    def stop(self):
        for _, resource in self._resources.items():
            resource.stop()
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def wait_until_finished(self):
        """ Blocks until the main thread is finished. """
        self._thread.join()

    def add_resource(self, resource_id, resource):
        self._resources[resource_id] = resource

    def add_subscriber_to_resource_publisher(self, resource_id, subscriber,
                                             *topics):
        if resource_id in self._resources:
            publisher = self._resources[resource_id].get_publisher()
            publisher.subscribe(subscriber, *topics)
            # logging.debug('Subscriber now subscribed to "%s" resource_id' +
            #               ' publisher for topics: [%s]', resource_id,
            #               ', '.join(topics))

    def add_resource_subscriber_to_publisher(self, resource_id, publisher,
                                             *topics):
        if resource_id in self._resources:
            subscriber = self._resources[resource_id].get_subscriber()
            publisher.subscribe(subscriber, *topics)
            # logging.debug('Publisher now has "%s" subscriber for topics: [%s]',
            #               resource_id, ', '.join(topics))
