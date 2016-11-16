# -*- coding: utf-8 -*-

# The parametrize function is generated, so this doesn't work:
#
#     from pytest.mark import parametrize
#
import pytest
parametrize = pytest.mark.parametrize

from duckomatic.platform.resources.rudder import (Rudder)


class TestRudder(object):

    @parametrize('rudder, min_rudder, max_rudder, expected', [
        (0, 0, 10, 0),
        (3, 0, 10, 3),
        (5, 0, 10, 5),
        (10, 0, 10, 10),
        (-1, 0, 10, 0),
        (11, 0, 10, 10)
    ])
    def test_validate_rudder(self, rudder, min_rudder, max_rudder, expected):
        assert Rudder.validate_rudder(
            rudder, min_rudder, max_rudder) == expected

    @parametrize('rudder, min_rudder, max_rudder, servo_min, \
        servo_max, expected', [
        (0, 0, 10, 100, 1000, 100),
        (3, 0, 10, 100, 1000, 370),
        (5, 0, 10, 100, 1000, 550),
        (10, 0, 10, 100, 1000, 1000),
        (-5, -5, 5, 245, 492, 245),
        (0, -5, 5, 245, 492, 368),
        (5, -5, 5, 245, 492, 492),
    ])
    def test_get_servo_value(self, rudder, min_rudder, max_rudder, servo_min,
                             servo_max, expected):
        assert Rudder.get_servo_value(
            rudder, min_rudder, max_rudder, servo_min, servo_max) == expected
