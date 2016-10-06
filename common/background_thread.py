import threading
from platform.main_controller import MainController
from platform.observer import Observer

class BackgroundThread(Observer):
	def __init__(self, socketio):
		super(BackgroundThread, self).__init__()
		self._socketio = socketio
		self._controller = MainController()
		self._controller.register(self)
		# self._thread = self._socketio.start_background_task(target=self.run)
		self._thread = threading.Thread(target=self.run, args=())
		self._thread.daemon = True
		self._thread.start()

	def run(self):
		"""Example of how to send server generated events to clients."""
		count = 0
		while True:
			message = self._messages.get()
			if 'namespace' in message['data']:
				self._socketio.emit(message['name'], message['data'], namespace=message['data']['namespace'])
			else:
				self._socketio.emit(message['name'], message['data'])
