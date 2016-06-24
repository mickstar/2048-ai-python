#! /usr/bin/python3

from sys import argv
import getopt

from ai.ai_runner import AIRunner
from game.humanplayer import HumanPlayer


def printHelp():
	print(
		"""Welcome to a 2048 game AI player
This program runs the 2048 game and attempts to make moves
./2048-ai [options] mode
modes:
	play		play a game on the console
	run			run AI iterations.
Options:
    -s          play silently and print a score
    -n X        run n iterations and print the best score
    -h          print this help message""")


def main():
	if len(argv) == 1:
		printHelp()
		return

	silentMode = False  # By default, we will always print the game state.
	iterations = 1  # By default, we only want to run once.

	try:
		opts, args = getopt.getopt(argv[1:], "hn:s", ["help", "iterations=", "silent"])
	except getopt.GetoptError as err:
		print(err)
		return

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			printHelp()
			return
		if opt in ("-n", "--iterations"):
			try:
				iterations = int(arg)
			except:
				print("Error {arg} is not a valid integer.".format(arg=arg))
				return

		if opt in ("-s", "--silent"):
			print("got -s")
			silentMode = True

	print(silentMode, iterations)
	if ("play" in argv):
		hp = HumanPlayer()
		hp.startGame()
	elif ("run" in argv):
		AIRunner(iterations=iterations, verbose=(not silentMode))


if __name__ == '__main__':
	main()
