from ai.ai_player import AIPlayer
from ai.random_ai import RandomAI


class AIRunner():
	'''Chooses from available AI modes which to run, and then executes it n many times.'''

	ai_options = {
		'random': RandomAI
	}

	def __init__(self, iterations=1, verbose=True):
		ai = self.get_ai_choice()

		self.performIterations(iterations, verbose, ai)

	def get_ai_choice(self):
		''' Will offer a selection of choices in the style of
			select ai:
			[0] option1
			[1] option2
			>>
		And will only finish once a valid input is received [0,1]
		Returns the class of the AI selected (as defined in above dict)'''
		print("Select an AI")
		options = list(self.ai_options)
		for i in range(len(options)):
			print("[{index}] {name}".format(index=i, name=options[i]))
		ret = input(">> ")
		try:
			if int(ret) in range(len(options)):
				return self.ai_options[options[int(ret)]]
		except:
			return self.get_ai_choice()

	def performIterations(self, iterations, verbose, ai):
		'''Runs the AI an arbritary number of times, each time recording the high score.
		At the end, the function will print the highest obtained score.
		'''
		scores = []
		for i in range(iterations):
			player = AIPlayer(ai)  # begins playing.
			score = player.startGame()
			print("Got score {score}".format(score=score))
			scores.append(score)
		print("Highest score was {max_score} from {n} iterations".format(max_score=max(scores), n=iterations))
