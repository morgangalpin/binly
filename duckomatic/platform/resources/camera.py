from duckomatic.utils.resource import Resource


class Camera(Resource):

    def __init__(self, *vargs, **kwargs):
        super(Camera, self).__init__(*vargs, **kwargs)
        self.count = 0

    def get_message_to_publish(self):
        self.count += 1
        return ('feed', {
            'url': 'fake://url',
            'count': self.count,
            'data': 'fake camera data'
        })

    def start(self):
        self.start_polling_for_messages_to_publish(0.01)
