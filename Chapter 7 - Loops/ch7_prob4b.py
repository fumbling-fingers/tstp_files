# Write a program with an infinite loop (with the option to type q to quit) 
# and a list of numbers. Each time through the loop ask the user to guess a 
# number on the list and tell them whether or not they guessed correctly.

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit. ")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit. ")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")
