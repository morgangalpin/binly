#!/usr/bin/env python
import os
from flask import Flask, render_template, session, request, send_from_directory
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, close_room, rooms, disconnect
from resources.camera import Camera
from resources.gps import Gps
from resources.rudder import Rudder
from resources.throttle import Throttle
from common.background_thread import BackgroundThread

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

static_dir = 'client/static'
app = Flask(__name__, template_folder=static_dir)
app.config['SECRET_KEY'] = 'RoboDuck!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


@app.route('/')
def index():
	global thread
	if thread is None:
		thread = BackgroundThread(socketio)
	return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/<path:filename>')
def serve_static(filename):
	return send_from_directory(static_dir, filename)

socketio.on_namespace(Camera('/camera'))
socketio.on_namespace(Gps('/gps'))
socketio.on_namespace(Rudder('/rudder'))
socketio.on_namespace(Throttle('/throttle'))


if __name__ == '__main__':
	socketio.run(app, debug=True)
