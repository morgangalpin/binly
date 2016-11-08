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

    def __init__(self):
        """ Constructor.
        Creates a thread and starts it immediately.
        """
        super(PlatformController, self).__init__()

        self._resources = {}
        self._thread = None
        self._stop = threading.Event()
        self._stop.set()

        self.add_resource('camera', Camera())
        self.add_resource('gps', Gps())
        self.add_resource('rudder', Rudder())
        self.add_resource('throttle', Throttle())

#     def run(self):
#         """ Method that runs forever """
#         count = 0
#         while not self.stopped():
#             # Just send a message periodically for now until reading from the
#             # queue is in place.
#             time.sleep(10)
#             count += 1
#             data = {'data': 'Server generated event',
#                     'count': count, 'num': 2}
#             topic = 'feed'
#             namespace = '/camera'
#             logging.debug('PlatformController: Sending: \
# topic: "%s", \
# data: "%s", \
# namespace: "%s"' %
#                           (topic, data, namespace))
#             self.socketio.emit(topic, data, namespace='/camera')
        # self.update('test', {
        #             'message': 'Server generated event',
        #             'count': count,
        #             'namespace': '/test'
        #             })
        # message = self._messages.get()
        # self.update_observers(message['name'], message['data'])

    def start(self):
        for _, resource in self._resources.items():
            resource.start()
        # if self.stopped():
        #     self._stop.clear()
        #     self._thread = threading.Thread(target=self.run, args=())
        #     self._thread.daemon = True
        #     self._thread.start()

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
