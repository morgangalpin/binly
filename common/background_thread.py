import threading
from platform.main_controller import MainController
from platform.observer import Observer

class BackgroundThread(Observer):
	def __init__(self, socketio):
		print "BackgroundThread.__init__() start"
		super(BackgroundThread, self).__init__()
		self._socketio = socketio
		print "BackgroundThread.__init__() here1"
		self._controller = MainController()
		print "BackgroundThread.__init__() here2"
		self._controller.register(self)
		print "BackgroundThread.__init__() here3"
		# self._thread = self._socketio.start_background_task(target=self.run)
		self._thread = threading.Thread(target=self.run, args=())
		self._thread.daemon = True
		self._thread.start()
		print "BackgroundThread.__init__() finish"

	def run(self):
		"""Example of how to send server generated events to clients."""
		count = 0
		while True:
			message = self._messages.get()
			self._socketio.emit(message['name'], message['data'])
