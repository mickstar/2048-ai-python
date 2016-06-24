import random

from ai.ai_interface import AbstractAIPlayer
from game.move import Move


class RandomAI (AbstractAIPlayer):
	def __init__(self):
		super().__init__()

	def makeMove(self, board):
		return random.choice([Move.LEFT_MOVE, Move.RIGHT_MOVE, Move.UP_MOVE, Move.DOWN_MOVE])