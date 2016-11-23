import logging
import os
import time
from duckomatic.utils.resource import Resource


class Camera(Resource):
    TIME_BETWEEN_IMAGE_PURGES_SECONDS = 5
    FRAMES_PER_SECOND = 4

    def __init__(self,
                 image_dir,
                 image_format='%d.jpg',
                 max_image_age_seconds=60,
                 fake=False,
                 *vargs, **kwargs):
        super(Camera, self).__init__(*vargs, **kwargs)
        self._image_num = 0
        self._image_dir = image_dir
        self._image_format = image_format
        self._max_image_age_seconds = max_image_age_seconds
        self._fake = fake
        self._remove_old_images_background_thread = None

    def get_message_to_publish(self):
        self._image_num += 1

        # Save the current image to the next file number.
        self._camera.capture(os.path.join(
            self._image_dir, self._image_format % (self._image_num)))

        # Notify listeners of the new image.
        return ('feed', {
            'image_id': self._image_num
        })

    def start(self):
        # Initialize the camera object.
        if self._fake:
            self._camera = FakePiCamera()
        else:
            # https://github.com/waveform80/picamera
            import picamera
            self._camera = picamera.PiCamera()
            self._camera.resolution = (320, 240)
        self.remove_old_images(0)
        self.start_remove_old_images_background_thread()
        self.start_polling_for_messages_to_publish(self.FRAMES_PER_SECOND)

    def start_remove_old_images_background_thread(self):
        self._remove_old_images_background_thread = self._start_thread(
            self._remove_old_images_background_thread,
            self.remove_old_images_in_background,
            ())

    def remove_old_images_in_background(self):
        while not self.stopped():
            self.remove_old_images(self._max_image_age_seconds)
            time.sleep(self.TIME_BETWEEN_IMAGE_PURGES_SECONDS)

    def remove_old_images(self, max_age_seconds):
        now = time.time()
        if os.path.isdir(self._image_dir):
            for filename in os.listdir(self._image_dir):
                file_path = os.path.join(self._image_dir, filename)
                try:
                    if os.path.isfile(file_path) \
                            and os.stat(file_path).st_mtime \
                            < now - max_age_seconds:
                        os.remove(file_path)
                except Exception as e:
                    logging.error(e)
        else:
            logging.debug(
                'Not removing images from "%s" because it is not \
a valid directory.' % self._image_dir)


class FakePiCamera(object):
    """ Implements the same interface as the Adafruit_Camera.Camera, but
    none of the methods do anything.
    """

    def __init__(self, *vargs, **kwargs):
        super(FakePiCamera, self).__init__(*vargs, **kwargs)

    def capture(
            self, output, format=None, use_video_port=False, resize=None,
            splitter_port=0, bayer=False, **options):
        logging.debug('FakePiCamera.capture(...)')
