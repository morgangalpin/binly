class Publisher(object):
    """
    A Publisher sends messages to a topic that has one or more
    Subscriber's subscribed to it. Topics can be subscribed to
    and unsubscribed from.
    """

    def __init__(self):
        super(Publisher, self).__init__()
        self._subscriptions = {}

    def subscribe(self, subscriber, *topics):
        """
        Subscribe the subscriber to the given list of topics.
        """
        subscriber_id = subscriber.get_id()
        for topic in topics:
            if topic not in self._subscriptions:
                self._subscriptions[topic] = {}
            if subscriber_id not in self._subscriptions[topic]:
                self._subscriptions[topic][subscriber_id] = subscriber

    def unsubscribe(self, subscriber, *topics):
        """
        Remove the subscriber's subscriptions to the given topics.
        """
        subscriber_id = subscriber.get_id()
        for topic in topics:
            if topic in self._subscriptions \
                    and subscriber_id in self._subscriptions[topic]:
                self._subscriptions[topic].pop(subscriber_id, None)

    def update(self, topic, data):
        """
        Publish data to a topic for all subscriber's on that topic.
        """
        # print(self._subscriptions)
        if topic in self._subscriptions:
            # print('Sending data to topic: %s, which has %d subscribers' %
            #       (topic, len(self._subscriptions[topic])))
            for subscriber in self._subscriptions[topic].itervalues():
                subscriber.update(topic, data)
