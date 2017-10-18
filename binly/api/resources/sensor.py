import logging
from binly.api.api_resource import ApiResource


class Sensor(ApiResource):

    def handle_incoming_message(self, topic, data):
        if self._client_count > 0:
            logging.debug('%s: Client count: %d, Sending: \
topic: "%s", \
data: "%s"' %
                          (self.namespace, self._client_count, topic, data))
            self.socketio.emit(
                topic, data, namespace=self.namespace)

    def start(self):
        self.start_processing_incoming_messages()
