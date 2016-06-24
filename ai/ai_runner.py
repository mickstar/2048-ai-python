from ai.ai_player import AIPlayer
from ai.random_ai import RandomAI


class AIRunner ():
	'''Upon execution, will offer to select an available AI.'''

	ai_options = {
		'random' : RandomAI
	}

	def __init__(self, iterations=1, verbose=True):
		ai = self.get_ai_choice ()

		self.performIterations(iterations, verbose, ai)

	def get_ai_choice(self):
		print ("Select an AI")
		options = list(self.ai_options)
		for i in range(len(options)):
			print ("[{index}] {name}".format(index=i, name=options[i]))
		ret = input (">> ")
		try:
			if int(ret) in range(len(options)):
				return self.ai_options[options[int(ret)]]
		except:
			return self.get_ai_choice()

	def performIterations(self, iterations, verbose, ai):
		scores = []
		for i in range(iterations):
			player = AIPlayer(ai) #begins playing.
			score = player.startGame()
			print ("Got score {score}".format(score=score))
			scores.append(score)
		print ("Highest score was {max_score} from {n} iterations".format(max_score=max(scores), n=iterations))

