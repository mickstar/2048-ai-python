class Cell:
	'''This class defines a cell in the 2048 grid.
	We will define an empty cell with value 0 or Cell.EMPTY'''

	def __init__(self, initialValue=None):
		if initialValue == None:
			self.value = Cell.EMPTY
		else:
			self.value = initialValue

	def __str__(self):
		return "%d" % (self.value)

	def isEmpty(self):
		return self.value == Cell.EMPTY

	def getValue(self):
		if (self.value == Cell.EMPTY):
			return 0
		return self.value

	def setValue(self, value):
		self.value = value

	def removeValue(self):
		self.value = Cell.EMPTY

	def doubleValue(self):
		self.value *= 2

	EMPTY = 0
