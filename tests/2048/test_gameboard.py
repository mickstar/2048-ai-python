import unittest

from game import gameboard
from game.gameboard import GameBoard
from game.humanplayer import HumanPlayer
from game.move import Move


class MyTestCase(unittest.TestCase):
	def test_create(self):
		gb = gameboard.GameBoard()
		self.assertTrue(gb.grid != None)

	def test_isEmpty(self):
		gb = GameBoard()
		self.assertTrue(gb.hasEmptyTiles())

	def test_getEmptyCells(self):
		gb = GameBoard()
		self.assertTrue(gb.getRandomlyAvailableCell() != None)

	def test_makeMove(self):
		gb = GameBoard()
		gb.getCell(0,0).setValue(2)
		gb.getCell(1,0).setValue(2)
		playable = gb.makeMove(Move.RIGHT_MOVE)
		self.assertTrue(playable)
		self.assertEqual(gb.getCell(3,0).getValue(),4)
		self.assertTrue(gb.getCell(1,0).isEmpty())
		self.assertTrue(gb.getCell(2,0).isEmpty())
		self.assertTrue(not gb.getCell(3,0).isEmpty())

	def test_makeMove2(self):
		gb = GameBoard()
		gb.getCell(1, 0).setValue(2)
		gb.getCell(2, 0).setValue(2)
		playable = gb.makeMove(Move.LEFT_MOVE)
		self.assertTrue(playable)
		self.assertEqual(gb.getCell(0, 0).getValue(), 4)
		self.assertTrue(gb.getCell(1, 0).isEmpty())
		self.assertTrue(gb.getCell(2, 0).isEmpty())
		self.assertTrue(gb.getCell(3, 0).isEmpty())

	def test_printGrid(self):
		gb = GameBoard()
		for x in range(4):
			for y in range(4):
				gb.getCell(x,y).setValue(y*4+x+1)
		print("Board should be [1,2,3,4],...,9]")
		gb.printBoard()

if __name__ == '__main__':
	unittest.main()
