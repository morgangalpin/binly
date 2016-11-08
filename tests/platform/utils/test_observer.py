# -*- coding: utf-8 -*-
from pytest import raises

# The parametrize function is generated, so this doesn't work:
#
#     from pytest.mark import parametrize
#
import pytest
parametrize = pytest.mark.parametrize

# from duckomatic import metadata
from duckomatic.platform.utils.observer import (Observer, NoMessageException)


class TestObserver(object):

    @parametrize('id_prefix', [
        '',
        'test123'
    ])
    def test_init(self, id_prefix):
        observer = Observer(id_prefix)
        assert type(observer) == Observer
        assert observer.get_id().startswith(id_prefix)

    @parametrize('message_name, data', [
        ('', {}),
        ('test123', {'test': 123})
    ])
    def test_update_and_simple_get_message(self, message_name, data):
        observer = Observer()
        observer.update(message_name, data)
        message = observer.get_message()
        assert message['name'] == message_name
        assert message['data'] == data

    @parametrize('timeout', [
        (0)
    ])
    def test_get_message_with_timeout(self, timeout):
        observer = Observer()
        with raises(NoMessageException):
            observer.get_message(timeout=timeout)
            # Should not get here as an exception should be raised.
            assert False
        # Exception was raised correctly.
        assert True

    @parametrize('id_prefix', [
        '',
        'test123'
    ])
    def test_get_id_is_unique(self, id_prefix):
        observer1 = Observer(id_prefix)
        observer2 = Observer(id_prefix)
        assert observer1.get_id() != observer2.get_id()
