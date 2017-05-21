import logging
from flask_socketio import (Namespace, emit)
# , join_room, leave_room, close_room,
#                         rooms, disconnect)
from binly.utils.resource import Resource


class Throttle(Resource, Namespace):

    def __init__(self, *vargs, **kwargs):
        """ Constructor.
        Initialize the parent classes.
        """
        super(Throttle, self).__init__(*vargs, **kwargs)
        self._client_count = 0

    def on_update(self, data):
        self._publisher.update('update', data)

    def on_connect(self):
        self._client_count += 1
        emit('clients', {'data': 'Connected',
                         'count': self._client_count})

    def on_disconnect(self):
        self._client_count -= 1
        logging.info('%s: Client disconnected. Client count = %d' %
                     (self.__class__, self._client_count))

    # def on_my_broadcast_event(self, message):
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': message['data'], 'count': session['receive_count']},
    #          broadcast=True)

    # def on_join(self, message):
    #     join_room(message['room'])
    #     session['receive_count'] = session.get('receive_count', 0) + 1
    #     emit('my_response',
    #          {'data': 'In Throttle rooms: ' + ', '.join(rooms()),
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
