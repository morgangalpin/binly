import logging
# from flask import session, request
from flask_socketio import (Namespace, emit)
# , join_room, leave_room, close_room,
#                         rooms, disconnect)
from binly.utils.resource import Resource


class Gps(Resource, Namespace):

    def __init__(self, *vargs, **kwargs):
        """ Constructor.
        Initialize the parent classes.
        """
        super(Gps, self).__init__(*vargs, **kwargs)
        self._client_count = 0

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
    #          {'data': 'In Gps rooms: ' + ', '.join(rooms()),
    #           'count': session['receive_count']})

    # def on_leave(self, message):
    #     leave_room(message['room'])
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': 'In rooms: ' + ', '.join(rooms()),
    #           'count': session['receive_count']})

    # def on_close_room(self, message):
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response', {'data': 'Room ' + message['room']
    #                          + ' is closing.',
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
