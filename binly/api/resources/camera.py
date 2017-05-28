import os
from binly.api.resources.sensor import Sensor


class Camera(Sensor):
    URL_KEY = 'url'
    IMAGE_ID_KEY = 'image_id'

    def __init__(self, image_path, *vargs, **kwargs):
        """ Constructor.
        Initialize the parent classes.
        """
        super(Camera, self).__init__(*vargs, **kwargs)
        self._image_path = image_path

    def handle_incoming_message(self, topic, data):
        if self._client_count > 0:
            # Add the image URL value to the data.
            if self.IMAGE_ID_KEY in data:
                data[self.URL_KEY] = os.path.join(
                    self._image_path, str(data[self.IMAGE_ID_KEY]))

            self.socketio.emit(
                topic, data, namespace=self.namespace)
