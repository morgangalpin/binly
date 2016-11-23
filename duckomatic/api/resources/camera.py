import logging
import os
# from flask import session, request
from flask_socketio import (Namespace, emit)
# , join_room, leave_room, close_room,
#                         rooms, disconnect)
from duckomatic.utils.resource import Resource


class Camera(Resource, Namespace):
    URL_KEY = 'url'
    IMAGE_ID_KEY = 'image_id'

    def __init__(self, image_path, *vargs, **kwargs):
        """ Constructor.
        Initialize the parent classes.
        """
        super(Camera, self).__init__(*vargs, **kwargs)
        self._client_count = 0
        self._image_path = image_path

    def handle_incoming_message(self, topic, data):
        if self._client_count > 0:
            # Add the image URL value to the data.
            if self.IMAGE_ID_KEY in data:
                data[self.URL_KEY] = os.path.join(
                    self._image_path, str(data[self.IMAGE_ID_KEY]))

            logging.debug('%s: Client count: %d, Sending: \
topic: "%s", \
data: "%s"' %
                          (self.namespace, self._client_count, topic, data))
            self.socketio.emit(
                topic, data, namespace=self.namespace)

    def start(self):
        self.start_processing_incoming_messages()

    def on_connect(self):
        self._client_count += 1
        emit('clients', {'data': 'Client connected',
                         'count': self._client_count})

    def on_disconnect(self):
        self._client_count -= 1
        print('%s: Client disconnected. Client count = %d' %
              (self.__class__, self._client_count))

    # def on_my_event(self, message):
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': message['data'], 'count': session['receive_count']})

    # def on_my_broadcast_event(self, message):
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': message['data'], 'count': session['receive_count']},
    #          broadcast=True)

    # def on_join(self, message):
    #     join_room(message['room'])
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': 'In Camera rooms: ' + ', '.join(rooms()),
    #           'count': session['receive_count']})

    # def on_leave(self, message):
    #     leave_room(message['room'])
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': 'In rooms: ' + ', '.join(rooms()),
    #           'count': session['receive_count']})

    # def on_close_room(self, message):
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response', {'data': 'Room ' + message['room'] +
    #                          ' is closing.',
    #                          'count': session['receive_count']},
    #          room=message['room'])
    #     close_room(message['room'])

    # def on_my_room_event(self, message):
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': message['data'], 'count': session['receive_count']},
    #          room=message['room'])

    # def on_disconnect_request(self):
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': 'Disconnected!', 'count': session['receive_count']})
    #     disconnect()

    # def on_my_ping(self):
    #     emit('my_pong')
