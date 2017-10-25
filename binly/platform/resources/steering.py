import logging
# from os.path import (dirname, abspath, join)
# import sys
from binly.utils.resource import Resource


class Steering(Resource):
    MIN_VALUE = -5
    MAX_VALUE = 5
    MIN_SCALE_VALUE = -1.0
    MAX_SCALE_VALUE = 1.0

    def __init__(self, *vargs, **kwargs):
        super(Steering, self).__init__(*vargs, **kwargs)
        self.value = 0

    def start(self):
        self.start_processing_incoming_messages()

    def handle_incoming_message(self, topic, value):
        logging.debug('Received Steering message on topic "%s": %s' %
                      (topic, value))

        # Validate the requested value.
        new_value = self.validate_value(
            'Steering',
            value, self.MIN_VALUE, self.MAX_VALUE)

        # Update the stored value and notify listeners of the scaled value.
        if new_value != self.value:
            self.value = new_value
            scaled_value = 1.0 - self.scale_float_value(
                self.value, self.MIN_VALUE, self.MAX_VALUE,
                self.MIN_SCALE_VALUE, self.MAX_SCALE_VALUE)
            self.get_publisher().update('scaled-steering', scaled_value)
