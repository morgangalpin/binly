import logging
import threading
import time
from duckomatic.utils.publisher import Publisher
from duckomatic.utils.subscriber import Subscriber


class Resource(object):

    def __init__(self, *vargs, **kwargs):
        super(Resource, self).__init__(*vargs, **kwargs)
        self._publisher = Publisher()
        self._subscriber = Subscriber()
        self._incoming_messages_thread = None
        self._outgoing_messages_thread = None
        self._stop = threading.Event()

    def get_publisher(self):
        return self._publisher

    def get_subscriber(self):
        return self._subscriber

    def handle_incoming_message(self, topic, data):
        """ This needs to be overridden by subclasses in order to handle
        messages on subscribed topics. """
        pass

    def get_message_to_publish(self):
        """ This needs to be overridden by subclasses in order to produce
        messages to be published. """
        return ('topic', {})

    @classmethod
    def _start_thread(cls, thread, target, args):
        if not thread:
            thread = threading.Thread(target=target, args=args)
            thread.daemon = True
            thread.start()
        return thread

    def start(self):
        pass

    def stop(self):
        # logging.debug('Stopping %s' % (self.__class__))
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def start_processing_incoming_messages(self):
        self._incoming_messages_thread = self._start_thread(
            self._incoming_messages_thread, self.process_incoming_messages,
            ())

    def process_incoming_messages(self):
        while not self.stopped():
            (topic, data) = self._subscriber.get_update()
            self.handle_incoming_message(topic, data)

    def start_polling_for_messages_to_publish(self, frequency_per_second):
        self._outgoing_messages_thread = self._start_thread(
            self._outgoing_messages_thread, self.poll_for_messages_to_publish,
            (frequency_per_second,))

    def poll_for_messages_to_publish(self, frequency_per_second):
        max_sleep_time = 1.0 / frequency_per_second
        while not self.stopped():
            t0 = time.time()
            (topic, data) = self.get_message_to_publish()
            # t1 = time.time()
            self._publisher.update(topic, data)
            # t2 = time.time()
#             logging.debug("%s: get_message_to_publish() took %fs. \
# Publisher.update() took %fs. Current time: %f" %
#                           (self.__class__, t1 - t0, t2 - t1, t2))
            sleep_time = max_sleep_time - (time.time() - t0)
            if sleep_time > 0:
                time.sleep(sleep_time)

    @staticmethod
    def validate_value(label, value, min_value, max_value):
        """ Validate the value value is between min_value and max_value.
        If it is beyond one of them, then return the min or max value,
        whichever is closest."""
        if value < min_value:
            logging.warning('%s value %d less than minimum value of %d. \
Setting to minimum.' % (label, value, min_value))
            return min_value
        if value > max_value:
            logging.warning('%s value %d greater than maximum value of \
%d. Setting to maximum.' % (label, value, max_value))
            return max_value
        return value

    @staticmethod
    def scale_value(source_value, min_source_value, max_source_value,
                    target_min, target_max):
        """ Calculate the target value for the given source_value. """
        return target_min + \
            int((float(source_value - min_source_value)
                 / float(max_source_value - min_source_value))
                * (target_max - target_min))
