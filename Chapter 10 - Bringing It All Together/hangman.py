# http://tinyurl.com/jhrvs94

import random
words = ["work","play","microsoft","fun","halloween","bravern"]

def hangman(word):
	wrong = 0
	stages = ["",
		   "________        ",
		   "|               ",
		   "|        |      ",
		   "|        O      ",
		   "|       /|\     ",
		   "|       / \     ",
		   "|               "
		   ]
	rletters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Welcome to Hangman!")

	while wrong < len(stages) - 1:
		print("\n")
		msg = "Guess a letter: "
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0: e]))
		if "__" not in board:
			print("\nYou win!\n")
			print(" ".join(board))
			win = True
			break

	if not win:
		print("\n".join(stages[0:wrong]))
		print("\n Sorry - You lose! The word was '{}'.".format(word))
		print("\n")


play = random.choice(words)
hangman(play)