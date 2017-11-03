# -*- coding: utf-8 -*-

# The parametrize function is generated, so this doesn't work:
#
#     from pytest.mark import parametrize
#
import pytest
from binly.platform.resources.servo import (Servo)

parametrize = pytest.mark.parametrize


class TestResource(object):

    @parametrize('start_value, end_value, max_rate, expected', [
        (0, 0, 5, [0]),
        (0, 5, 5, [0, 5]),
        (0, 10, 5, [0, 5, 10]),
        (5, 0, 5, [5, 0]),
        (10, 0, 5, [10, 5, 0])
    ])
    def test_smooth_value_series(self, start_value, end_value,
                                 max_rate, expected):
        assert Servo.smooth_value_series(
            start_value, end_value, max_rate).tolist() == expected
