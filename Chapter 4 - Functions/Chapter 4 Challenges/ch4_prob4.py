# write a program with two functions. 

# the first function should take an integer as a parameter and 
# return the result of the integer divided by 2. 

# the second function should take an interger as a parameter and
# return the result of the integer multiplied by 4. 

# Call the first function, save the result as a variable, and
# pass it as a parameter to the second function.

def divide(x):
    return x / 2

def mutltiply(y):
    return y * 4

num1 = divide(16)
num2 = mutltiply(num1)

print(num2)

num3 = divide(32)
num4 = mutltiply(num3)

print(num4)