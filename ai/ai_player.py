from ai.ai_interface import AbstractAIPlayer
from game.gamemanager import GameManager


class AIPlayer ():
	'''
	This class, given an AI, plays it and outputs the score.
	'''

	def __init__(self, ai_instance, verbose=True):
		assert (issubclass(ai_instance, AbstractAIPlayer))
		self.ai = ai_instance()

		self.verbose = verbose
		self.game = GameManager()

		self.startGame()

	def startGame (self):
		self.game.initialize()
		playable = True
		while (playable):
			if (self.verbose):
				self.game.outputGame()
			playable = self.move()


	def move (self):
		grid = self.game.getBoard()
		move = self.ai.makeMove(board=grid)
		playable = self.game.makeMove(move)
		if (not playable):
			if (not self.game.isGameTerminated()):
				return self.move()
			else:
				return False
		return playable