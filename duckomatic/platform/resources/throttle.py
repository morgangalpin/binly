import logging
from duckomatic.utils.resource import Resource


class Throttle(Resource):

    def __init__(self, *vargs, **kwargs):
        super(Throttle, self).__init__(*vargs, **kwargs)

    def handle_incoming_message(self, topic, data):
        logging.debug('Received message on topic "%s": %s' % (topic, data))

    def start(self):
        self.start_processing_incoming_messages()
