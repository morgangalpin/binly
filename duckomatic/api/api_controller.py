#!/usr/bin/env python
from flask import (Flask, render_template,
                   send_from_directory)
from flask_socketio import (SocketIO)
from duckomatic.platform.platform_controller import PlatformController
from resources.camera import Camera
# from resources.gps import Gps
# from resources.rudder import Rudder
# from resources.throttle import Throttle

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to
# choose the best option based on installed packages.
async_mode = None
static_dir = 'client/static'


def subscribe_from_platform_resource(socketio, platform_controller,
                                     api_resource_namespace,
                                     platform_resource_name, *topics):
    platform_controller.subscribe_from_resource(
        platform_resource_name, api_resource_namespace.get_subscriber(),
        *topics)
    socketio.on_namespace(api_resource_namespace)


def subscribe_to_platform_resource(socketio, platform_controller,
                                   api_resource_namespace,
                                   platform_resource_name, *topics):
    platform_controller.subscribe_to_resource(
        platform_resource_name, api_resource_namespace.get_publisher(),
        *topics)
    socketio.on_namespace(api_resource_namespace)


app = Flask(__name__, template_folder=static_dir)
app.config['SECRET_KEY'] = 'RoboDuck!'
socketio = SocketIO(app, async_mode=async_mode)

platform_controller = PlatformController()
subscribe_from_platform_resource(
    socketio, platform_controller, Camera('/camera'), 'camera', 'feed')
# subscribe_from_platform_resource(
#     socketio, platform_controller, Gps('/gps'), 'gps', 'feed')
# subscribe_to_platform_resource(
#     socketio, platform_controller, Rudder('/rudder'), 'rudder', 'feed')
# subscribe_to_platform_resource(
#     socketio, platform_controller, Throttle('/throttle'), 'throttle', 'feed')


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(static_dir, filename)


if __name__ == '__main__':
    socketio.run(app, debug=True)
