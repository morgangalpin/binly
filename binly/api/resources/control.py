from binly.api.api_resource import ApiResource


class Control(ApiResource):

    def on_update(self, data):
        self._publisher.update('update', data)
