import random

from game.cell import Cell
from game.move import Move


class GameBoard:
	size = 4

	def __init__(self):
		self.grid = [[Cell(Cell.EMPTY) for x in range(GameBoard.size)] for x in range(GameBoard.size)]

	def printBoard(self):
		for y in range(GameBoard.size):
			for x in range(GameBoard.size):
				cell = self.getCell(x,y)
				print(cell, end="\t")
			print("")  # new line

	def hasEmptyTiles(self):
		for row in self.grid:
			for cell in row:
				if cell.isEmpty():
					return True

		return False

	# return cell at the (x,y) coordinates.
	# grid is structured such that the top left corner is (0,0)
	# likewise, the bottom right is (3,3)
	def getCell(self,x,y):
		return self.grid[x][y]

	def getRandomlyAvailableCell(self):
		emptyCells = []
		for row in self.grid:
			for cell in row:
				if cell.isEmpty():
					emptyCells.append(cell)

		return random.choice(emptyCells)


	# modifies the grid such in the direction of the move.
	# Such that Right[0,2,2,0] -> [0,0,0,4]
	# for each horizontal row in grid
	def makeMove(self, move):
		x_delta = 0
		y_delta = 0
		n = GameBoard.size
		x_range = list(range(n))
		y_range = list(range(n))
		if move == Move.LEFT_MOVE:
			x_delta = -1
			x_range = list(reversed(range(n)))
		if move == Move.RIGHT_MOVE:
			x_delta = +1
		if move == Move.UP_MOVE:
			y_delta = -1
			x_range = list(reversed(range(n)))
		if move == Move.DOWN_MOVE:
			y_delta = +1

		successfullyMoved = False
		score_delta = 0

		for x in x_range:
			joinedAt = 0
			for y in y_range:
				#first we check to see we are not on an edge cell.
				if (x+x_delta) in x_range and (y+y_delta) in y_range:
					curCell = self.getCell(x,y)
					adjCell = self.getCell(x+x_delta, y+y_delta)

					#Check to see if we can merge two cells, e.g RIGHT[0,0,2,2] -> [0,0,0,4]
					if (not curCell.isEmpty()
						and curCell.getValue() != joinedAt
						and curCell.getValue() == adjCell.getValue()):

						joinedAt = curCell.getValue()
						successfullyMoved = True
						score_delta += curCell.value
						adjCell.doubleValue()
						curCell.removeValue()

					#Check to see if we can move a cell e.g RIGHT[2,0,0,0] -> [0,2,0,0]
					elif not curCell.isEmpty() and adjCell.isEmpty():
						successfullyMoved = True
						adjCell.setValue(curCell.value)
						curCell.removeValue()
		return successfullyMoved, score_delta




	def hasMovesAvailable (self):
		if (self.hasEmptyTiles()):
			return True
		n = len(self.grid)
		for (x_delta,y_delta) in [(0,1),(0,-1),(1,0), (-1,0)]:
			x_range = list(range(n))
			y_range = list(range(n))
			if x_delta == -1:
				x_range = reversed(x_range)
			if y_delta == -1:
				y_range = reversed(y_range)
			for x in x_range:
				for y in y_range:
					curCell = self.getCell(x,y)
					adjCell = self.getCell(x+x_delta,y_delta)
					if (curCell.value == adjCell.value):
						return True # a move is available.
		return False
