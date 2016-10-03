from Queue import Queue

class Observer(object):
	"""
		Implements a subscribe interface for objects to monitor Observables.
	"""
	
	def __init__(self):
		super(Observer, self).__init__()
		self._messages = Queue()

	def update(self, message_name, data):
		""" Queue the message and data to be sent to deal with later. """
		self._messages.put({'name': message_name, 'data': data})
