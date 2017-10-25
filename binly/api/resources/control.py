import logging
from binly.api.api_resource import ApiResource


class Control(ApiResource):

    def __init__(self, topic='update', *vargs, **kwargs):
        """ Constructor.
        Initialize the parent classes.
        """
        super(Control, self).__init__(*vargs, **kwargs)
        self.topic = topic
        logging.debug("Control sending updates to topic: %s", self.topic)

    def on_update(self, data):
        logging.debug("Control sending update to topic: %s", self.topic)
        self._publisher.update(self.topic, data)
