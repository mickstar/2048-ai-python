import unittest

from game.cell import Cell


class TestCell(unittest.TestCase):
	def test_create(self):
		cell = Cell()
		self.assertEqual(cell.getValue(), Cell.EMPTY)
		cell = Cell(123123)
		self.assertEqual(cell.getValue(), 123123)

	def test_removeValue(self):
		cell = Cell(2)
		self.assertEqual(cell.getValue(), 2)
		cell.removeValue()
		self.assertEqual(cell.getValue(), 0)

	def test_setValue(self):
		cell = Cell(Cell.EMPTY)
		cell.setValue(123)
		self.assertTrue(cell.getValue(), 123)
		cell.setValue(2)
		self.assertTrue(cell.getValue(), 2)

	def test_isEmpty(self):
		cell = Cell(Cell.EMPTY)
		self.assertTrue(cell.isEmpty())
		cell.setValue(2)
		self.assertTrue(not cell.isEmpty())

if __name__ == '__main__':
	unittest.main()
