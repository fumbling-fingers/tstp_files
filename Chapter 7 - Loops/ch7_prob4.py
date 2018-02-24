# Write a program with an infinite loop (with the option to type q to quit) 
# and a list of numbers. Each time through the loop ask the user to guess a 
# number on the list and tell them whether or not they guessed correctly.

numbers = [4,7,13,14,21,76,94]

guess = input("guess a number or press 'q' to quit: ")

while guess != 'q':
    if int(guess) in numbers:
        print("you guessed correctly!")
        print("")
        guess = input("guess again or press 'q' to quit: ")
        
    else:
        print("you guessed wrong!")
        print("")
        guess = input("guess again or press 'q' to quit: ")
        