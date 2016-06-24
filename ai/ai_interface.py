from abc import ABCMeta,abstractmethod

class AbstractAIPlayer(metaclass=ABCMeta):
	'''
	this is an interface demonstrating what methods should be implemented by a 2048 AI
	'''

	@abstractmethod
	def __init__ (self):
		pass

	@abstractmethod
	def makeMove (self, board):
		pass


