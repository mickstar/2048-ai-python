from game.gamemanager import GameManager
from game.move import Move


class HumanPlayer:
	def __init__(self):
		self.game = GameManager()


	def startGame(self):
		self.game.initialize()
		self.makeMove()

	def makeMove(self):
		self.game.outputGame()
		move_t = self.getUserMove()
		if move_t == 'L': move = Move.LEFT_MOVE
		if move_t == 'R': move = Move.RIGHT_MOVE
		if move_t == 'U': move = Move.UP_MOVE
		if move_t == 'D': move = Move.DOWN_MOVE
		playable = self.game.makeMove(move)
		if playable:
			self.makeMove()
		else:
			self.startGame()



	def getUserMove(self):
		move_input = input ("Make your move [L,R,U,D]>>").strip().upper()
		if (move_input not in ['L','R','U','D']):
			print ("Error {move} not recognized".format(move=move_input))
			return self.getUserMove()

		return move_input
