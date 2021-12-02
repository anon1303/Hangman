import random
import string

def game(ans):
	life = 10
	guess = ''
	
	while True:
		blanks = '' #string that will contain the correctly guessed letter
		
		# concatonate the correct letter to the main string
		#if the letter is in the WORD 
		#find where is the location of the letter and concatonate
		for i in ans:
			if i in guess:
				blanks = blanks + i

			else:
				blanks = blanks + "_" + " "

		# When the player got the correct Word
		if blanks == ans:
			print(blanks.upper())
			print("")
			print("*"*14)
			print("YOU WIN!")
			print("*"*14)

			break

		#player input a guess letter
		print("Guess the word: ", blanks)
		a = input().lower()

		#check if the input correct(is in the alphabet)
		if a.isalpha():
			guess = guess + a
		else:
			print("Invalid character")
			a = input().lower()

		if a not in ans:
			life = life - 1
			if life == 9:
				print("9 life left")
				print("  --------  ")
			if life == 8:
				print("8 life left")
				print("  --------  ")
				print("     O      ")
			if life == 7:
				print("7 life left")
				print("  --------  ")
				print("     O      ")
				print("     |      ")
			if life == 6:
				print("6 life left")
				print("  --------  ")
				print("     O      ")
				print("     |      ")
				print("    /       ")
			if life == 5:
				print("5 life left")
				print("  --------  ")
				print("     O      ")
				print("     |      ")
				print("    / \     ")
			if life == 4:
				print("4 life left")
				print("  --------  ")
				print("   \ O      ")
				print("     |      ")
				print("    / \     ")
			if life == 3:
				print("3 life left")
				print("  --------  ")
				print("   \ O /    ")
				print("     |      ")
				print("    / \     ")
			if life == 2:
				print("2 life left")
				print("  --------  ")
				print("   \ O /|   ")
				print("     |      ")
				print("    / \     ")
			if life == 1:
				print("1 life left")
				print("Last breaths counting, Take care!")
				print("  --------  ")
				print("   \ O_|/   ")
				print("     |      ")
				print("    / \     ")
			if life == 0:
				print("You loose")
				print("You let a kind man die")
				print("  --------  ")
				print("     O_|    ")
				print("    /|\      ")
				print("    / \     ")
				print("\nThe word is",ans.upper())
				break
while True:

	#Chose a random word from a list of words from
	#the text file				
	with open('words.txt') as words:
		chosen = [word for word in words]
		c = random.choice(chosen)

		word = c.rstrip()

	print("*"*17)
	print("  H A N G M A N")
	print("*"*17)

	name = input("Enter your name: \n") #Ask player's name
	print("Welcome",name.upper(),"enjoy and don't let paga die!")

	# words = random.choice(["water","black","nature","ant","party"]) #library of words

	print("_"*50)
	print("try to guess the word in less than 10 attempts!")
	game(word)