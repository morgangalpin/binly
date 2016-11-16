import eventlet
import logging
from flask import (Flask, render_template,
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

    def __init__(self):
        super(ApiController, self).__init__()

        # Set this variable to "threading", "eventlet" or "gevent" to test the
        # different async modes, or leave it set to None for the application to
        # choose the best option based on installed packages.
        self._async_mode = "eventlet"

        self._resources = {}

        self._static_dir = '../../client/static'
        self._app = Flask(__name__, template_folder=self._static_dir)
        self._app.config['SECRET_KEY'] = 'Duckomatic!'
        self._app.route('/', methods=['GET'])(self.index)
        self._app.route('/<path:filename>', methods=['GET'])(self.serve_static)

        self._socketio = SocketIO(self._app, async_mode=self._async_mode)
        self.add_namespace_resource('camera', Camera('/camera'))
        self.add_namespace_resource('gps', Gps('/gps'))
        self.add_namespace_resource('rudder', Rudder('/rudder'))
        self.add_namespace_resource('throttle', Throttle('/throttle'))

    # @app.route('/')
    def index(self):
        return render_template('index.html',
                               async_mode=self._socketio.async_mode)

    # @app.route('/<path:filename>')
    def serve_static(self, filename):
        return send_from_directory(self._static_dir, filename)

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
