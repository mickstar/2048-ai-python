import unittest

from game.gameboard import GameBoard
from game.gamemanager import GameManager


class MyTestCase(unittest.TestCase):
	def test_initialize(self):
		game = GameManager()
		game.initialize()
		board = game.getBoard()
		# Test to see if we have the case of 2 numbers that are either 2 or 4
		self.assertTrue(sum(map(sum, board)) in [4,6,8])

		# test to see if there are exactly 2 non zero elements in the board.
		self.assertEqual(
			sum(
				map(lambda row:
					len(list(filter(lambda n : n != 0, row))), board)
			), 2)

	def test_getBoard(self):
		game =  GameManager()
		game.initialize()
		gb = game.gameboard
		for x in range(4):
			for y in range(4):
				gb.getCell(x, y).setValue(y * 4 + x + 1)

		grid = game.getBoard()
		self.assertEqual(grid, ((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,16)))

	def test_isGameTerminated(self):
		game = GameManager()
		game.gameboard.getCell(0,0).setValue(2)
		game.gameboard.getCell(1,0).setValue(4)
		game.gameboard.getCell(2,0).setValue(8)
		game.gameboard.getCell(3,0).setValue(16)

		game.gameboard.getCell(0,1).setValue(4)
		game.gameboard.getCell(1,1).setValue(2)
		game.gameboard.getCell(2,1).setValue(128)
		game.gameboard.getCell(3,1).setValue(8)

		game.gameboard.getCell(0,2).setValue(128)
		game.gameboard.getCell(1,2).setValue(8)
		game.gameboard.getCell(2,2).setValue(2)
		game.gameboard.getCell(3,2).setValue(4)

		game.gameboard.getCell(0,3).setValue(256)
		game.gameboard.getCell(1,3).setValue(2)
		game.gameboard.getCell(2,3).setValue(16)
		game.gameboard.getCell(3,3).setValue(2)

		self.assertTrue(game.isGameTerminated())



if __name__ == '__main__':
	unittest.main()
