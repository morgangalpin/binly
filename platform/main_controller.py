import threading
import time
from observable import Observable
from observer import Observer

class MainController(Observable, Observer):
	""" Main controller for the robot platform.
	The run() method will be started and it will run in the background
	until the application exits.
	"""

	def __init__(self):
		""" Constructor.
		Creates a thread and starts it immediately.
		"""
		super(MainController, self).__init__()
		self._thread = threading.Thread(target=self.run, args=())
		self._thread.daemon = True
		self._thread.start()

	def run(self):
		""" Method that runs forever """
		count = 0
		while True:
			# Just send a message periodically for now until reading from the queue is in place.
			time.sleep(10)
			count += 1
			self.update('test', {'message': 'Server generated event', 'count': count, 'namespace': '/test'})
			message = self._messages.get()
			self.update_observers(message['name'], message['data'])
