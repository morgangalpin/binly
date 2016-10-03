class Observable(object):
	""" An object that can be observed. Observers register themselves with the Observer,
	then the Observer updates the Observers when there is an event.
	"""

	def __init__(self):
		print "Observable.__init__() start"
		super(Observable, self).__init__()
		self._observers = []
		print "Observable.__init__() finish"

	def register(self, observer):
		"""
		The observer must implement the update(*args, **kwargs) method. This is called when 
		there is an event.
		"""
		if not observer in self._observers:
			self._observers.append(observer)

	def unregister(self, observer):
		if observer in self._observers:
			self._observers.remove(observer)

	def unregister_all(self):
		if self._observers:
			del self._observers[:]

	def update_observers(self, message_name, data):
		for observer in self._observers:
			observer.update(message_name, data)
