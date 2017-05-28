# -*- coding: utf-8 -*-

# The parametrize function is generated, so this doesn't work:
#
#     from pytest.mark import parametrize
#
import pytest
parametrize = pytest.mark.parametrize

# from binly import metadata
from binly.utils.publisher import (Publisher)


class TestPublisher(object):

    def test_init(self):
        publisher = Publisher()
        assert type(publisher) == Publisher

    @parametrize('topics, data', [
        (['topic1'], {'test': 123}),
        (['topic1', 'topic2'], {'test': 123})
    ])
    def test_subscribe_then_publish(self, topics, data):
        publisher = Publisher()
        subscriber = MockSubscriber('subscriber')
        publisher.subscribe(subscriber, *topics)
        publisher.update(topics[0], data)
        updates = subscriber.get_updates()
        assert len(updates) == 1
        (actual_topic, actual_data) = updates[0]
        assert actual_topic == topics[0]
        assert actual_data == data

    @parametrize('topics, data', [
        (['topic1'], {'test': 123}),
        (['topic1', 'topic2'], {'test': 123})
    ])
    def test_unsubscribe(self, topics, data):
        publisher = Publisher()
        subscriber = MockSubscriber('subscriber')
        publisher.subscribe(subscriber, *topics)
        publisher.unsubscribe(subscriber, topics[0])
        publisher.update(topics[0], data)
        updates = subscriber.get_updates()
        assert len(updates) == 0


class MockSubscriber(object):

    def __init__(self, id):
        super(MockSubscriber, self).__init__()
        self._id = id
        self._updated_data = []

    def get_id(self):
        return self._id

    def update(self, topic, data):
        self._updated_data.append((topic, data))

    def get_updates(self):
        return self._updated_data
