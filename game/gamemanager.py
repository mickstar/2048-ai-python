from game.gameboard import GameBoard
from game.move import Move
import random


class GameManager:
	n_starting_cells = 2

	def __init__(self):
		self.gameboard = GameBoard()

	def initialize(self):
		self.score = 0
		for x in range(GameManager.n_starting_cells):
			self.addRandomTile(value=2)

	def outputGame(self):
		print("Current Score is {score}".format(score=self.score))
		self.gameboard.printBoard()

	# Returns a copy of the 2d tuple of the grid
	# s.t grid = ((1,2,3,4), ..., (13,14,15,16))
	def getBoard(self):
		row = lambda y : tuple(self.gameboard.getCell(x,y).getValue() for x in range(self.gameboard.size))
		return tuple(row(y) for y in range(self.gameboard.size))



	# adds a 2 or 4 in an empty cell.
	def addRandomTile(self, value=None):
		if self.gameboard.hasEmptyTiles():
			if (value == None):
				new_value = 2 if random.random() < 0.9 else 4
			else:
				new_value = value
			cell = self.gameboard.getRandomlyAvailableCell()
			cell.setValue(new_value)

	def finishGame(self):
		print("Game over, final score: {score}".format(score=self.score))
		self.gameboard.printBoard()

	def makeMove(self, move):
		assert (move in [Move.LEFT_MOVE, Move.RIGHT_MOVE, Move.UP_MOVE, Move.DOWN_MOVE])
		status, score_diff = self.gameboard.makeMove(move)
		if (status == False):
			return False

		self.score += score_diff
		self.addRandomTile()
		if self.isGameTerminated():
			self.finishGame()
			return False
		return True

	def isGameTerminated(self):
		return not self.gameboard.hasMovesAvailable()