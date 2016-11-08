# -*- coding: utf-8 -*-
from pytest import raises

# The parametrize function is generated, so this doesn't work:
#
#     from pytest.mark import parametrize
#
import pytest
parametrize = pytest.mark.parametrize

# from duckomatic import metadata
from duckomatic.utils.subscriber import (Subscriber, NoDataException)


class TestSubscriber(object):

    @parametrize('id_prefix', [
        '',
        'test123'
    ])
    def test_init(self, id_prefix):
        subscriber = Subscriber(id_prefix)
        assert type(subscriber) == Subscriber
        assert subscriber.get_id().startswith(id_prefix)

    @parametrize('topic, data', [
        ('', {}),
        ('test123', {'test': 123})
    ])
    def test_update_and_simple_get_update(self, topic, data):
        subscriber = Subscriber()
        subscriber.update(topic, data)
        (actual_topic, actual_data) = subscriber.get_update()
        assert actual_topic == topic
        assert actual_data == data

    @parametrize('timeout', [
        (0)
    ])
    def test_get_update_with_timeout(self, timeout):
        subscriber = Subscriber()
        with raises(NoDataException):
            subscriber.get_update(timeout=timeout)
            # Should not get here as an exception should be raised.
            assert False
        # Exception was raised correctly.
        assert True

    @parametrize('id_prefix', [
        '',
        'test123'
    ])
    def test_get_id_is_unique(self, id_prefix):
        subscriber1 = Subscriber(id_prefix)
        subscriber2 = Subscriber(id_prefix)
        assert subscriber1.get_id() != subscriber2.get_id()
