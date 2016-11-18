# import logging
import threading

from duckomatic.platform.resources.camera import Camera
from duckomatic.platform.resources.gps import Gps
from duckomatic.platform.resources.rudder import Rudder
from duckomatic.platform.resources.throttle import Throttle


class PlatformController(object):
    """ Main controller for the robot platform.
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, fake=False):
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

        self.add_resource('camera', Camera())
        self.add_resource('gps', Gps())
        self.add_resource('rudder', Rudder(fake=self.fake))
        self.add_resource('throttle', Throttle(fake=self.fake))

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

    def add_resource_subscriber_to_publisher(self, resource_id, publisher,
                                             *topics):
        if resource_id in self._resources:
            subscriber = self._resources[resource_id].get_subscriber()
            publisher.subscribe(subscriber, *topics)
