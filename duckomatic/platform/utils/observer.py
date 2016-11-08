import Queue
import threading


class Observer(object):
    """
        Implements a subscribe interface for objects to monitor Observables.
    """

    _id_sequence = 0
    _id_sequence_lock = threading.Lock()

    def __init__(self, id_prefix=''):
        super(Observer, self).__init__()
        self._messages = Queue.Queue()
        self.id = id_prefix + str(self._get_next_id_sequence())

    def update(self, message_name, data):
        """ Queue the message and data to be sent to deal with later. """
        self._messages.put({'name': message_name, 'data': data})

    def get_message(self, timeout=None):
        """
        Get the oldest queued message. If there are no messages, this
        will block until there is one.

        Keyword arguments:
            timeout: The maximum number of seconds to block when waiting for
                     a message to be available. Defaults to None, which will
                     wait indefinitely. If a timeout occurs, the
                     NoMessageException exception is raised.
        """
        try:
            return self._messages.get(timeout=timeout)
        except Queue.Empty:
            raise NoMessageException(
                'No messages are available after timeout %d \
                seconds' % (timeout))

    @classmethod
    def _get_next_id_sequence(cls):
        with cls._id_sequence_lock:
            cls._id_sequence += 1
            return cls._id_sequence

    def get_id(self):
        """ Get the unique id for the Observer instance. """
        return self.id


class NoMessageException(Exception):
    """
    Raised by Observer.get_message() when a timeout is specified and no
    messages are available.
    """
    pass
