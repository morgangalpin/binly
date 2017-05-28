import Queue
import threading


class Subscriber(object):
    """
        Implements a subscribe interface for objects to monitor Publishers.
    """

    _id_sequence = 0
    _id_sequence_lock = threading.Lock()

    def __init__(self, id_prefix=''):
        super(Subscriber, self).__init__()
        self._messages = Queue.Queue()
        self.id = id_prefix + str(self._get_next_id_sequence())

    def update(self, topic, data):
        """ Queue the message and data to be sent to deal with later. """
        self._messages.put((topic, data))

    def get_update(self, timeout=None):
        """
        Get the oldest queued data. If there is no data, either block until
        there is one, or if timout is given, block for that many seconds.
        If there is already data waiting, the method will return immediately
        without blocking.

        Keyword arguments:
            timeout: The maximum number of seconds to block when waiting for
                     data to be available. Defaults to None, which will
                     wait indefinitely. If a timeout occurs, the
                     NoDataException exception is raised.
        """
        try:
            return self._messages.get(timeout=timeout)
        except Queue.Empty:
            raise NoDataException(
                'No data is available after timeout %d \
                seconds' % (timeout))

    @classmethod
    def _get_next_id_sequence(cls):
        with cls._id_sequence_lock:
            cls._id_sequence += 1
            return cls._id_sequence

    def get_id(self):
        """ Get the unique id for the Subscriber instance. """
        return self.id


class NoDataException(Exception):
    """
    Raised by Subscriber.get_update() when a timeout is specified and no
    data is available.
    """
    pass
