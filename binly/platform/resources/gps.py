from duckomatic.utils.resource import Resource


class Gps(Resource):

    def __init__(self, *vargs, **kwargs):
        super(Gps, self).__init__(*vargs, **kwargs)
        self.count = 0
        self.latitude = 49.289324
        self.longitude = -123.129219

    def get_message_to_publish(self):
        self.count += 1
        self.latitude += 0.000001
        self.longitude += 0.000001
        return ('feed', {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'count': self.count
        })

    def start(self):
        self.start_polling_for_messages_to_publish(0.01)
