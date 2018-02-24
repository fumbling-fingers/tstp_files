# error message

# function definitions, no parameters required
def err_msg():
	print("Oooops! Sorry, can't do that")

def user_err():
	print("code that user did not follow")
	err_msg()

# function definiton with parameters
"""
takes in an integer from the user and outputs
that value of that integer cubed
"""

def cube_it(y):
	return y ** 3

# your program

print("") # prints empty string
print("Fake beginning of program")
user_err()

err_msg()

print("")
output = cube_it(2)
print(output)

output2 = cube_it(100)
print(output2)

print("\nFake middle of program")
user_err()
err_msg()

print("")
for numbers in range(0,51,25):
	print(numbers) # \n

print("\nFake end of program")
user_err()
err_msg()

output = 10
print(output)