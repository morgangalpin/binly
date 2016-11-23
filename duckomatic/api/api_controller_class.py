import eventlet
import logging
import os
from flask import (Flask,
                   send_from_directory)
from flask_socketio import (SocketIO)
from resources.camera import Camera
from resources.gps import Gps
from resources.rudder import Rudder
from resources.throttle import Throttle

logging.basicConfig(level=logging.DEBUG)
eventlet.monkey_patch()


class ApiController(object):
    """
    Starts up and handles the websocket api.
    """
    CAMERA1_IMAGE_PATH = '/camera1/image'

    def __init__(self, camera1_image_dir, camera_image_format='%d.jpg',
                 camera1_image_max_age_seconds=60):
        super(ApiController, self).__init__()

        # Set this variable to "threading", "eventlet" or "gevent" to test the
        # different async modes, or leave it set to None for the application to
        # choose the best option based on installed packages.
        self._async_mode = "eventlet"

        self._resources = {}

        self._camera_image_format = camera_image_format
        self._static_dir = os.path.join(
            os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))),
            'client', 'static')
        self._camera1_image_dir = camera1_image_dir
        self._camera1_image_max_age_seconds = camera1_image_max_age_seconds
        self._app = Flask(
            __name__,
            static_folder=self._static_dir,
            static_url_path='/static')
        self._app.config['SECRET_KEY'] = 'Duckomatic!'
        self._app.add_url_rule('/', 'index', self.index)
        self._app.add_url_rule(
            os.path.join(self.CAMERA1_IMAGE_PATH, '<int:imagenum>'),
            'camera1', self.serve_camera_image)

        self._socketio = SocketIO(self._app, async_mode=self._async_mode)
        self.add_namespace_resource('camera', Camera(
            self.CAMERA1_IMAGE_PATH, '/camera'))
        self.add_namespace_resource('gps', Gps('/gps'))
        self.add_namespace_resource('rudder', Rudder('/rudder'))
        self.add_namespace_resource('throttle', Throttle('/throttle'))

    # @app.route('/')
    def index(self):
        return send_from_directory(self._static_dir, 'index.html')

    # @app.route('/camera1/image/<int:imagenum>')
    def serve_camera_image(self, imagenum):
        filename = self._camera_image_format % imagenum
        logging.debug("Sending camera image: %s" % filename)
        return send_from_directory(
            self._camera1_image_dir,
            filename,
            cache_timeout=self._camera1_image_max_age_seconds,
            add_etags=False, mimetype='image/jpeg')

    def start(self, start_resources, debug=False):
        if start_resources:
            logging.debug("Starting api resources")
            for _, resource in self._resources.items():
                resource.start()
        self._socketio.run(self._app, debug=debug, host='0.0.0.0')

    def stop(self):
        for _, resource in self._resources.items():
            resource.stop()

    def add_namespace_resource(self, resource_id, namespace_resource):
        self._resources[resource_id] = namespace_resource
        self._socketio.on_namespace(namespace_resource)

    def get_resource_subscriber(self, resource_id):
        return self._resources[resource_id].get_subscriber()

    def get_resource_publisher(self, resource_id):
        return self._resources[resource_id].get_publisher()
