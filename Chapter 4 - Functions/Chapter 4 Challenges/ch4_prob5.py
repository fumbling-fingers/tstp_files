# Write a function that converts a string to a float
# and returns the result. Use exception handling to
# catch the exception that could occur.

def str_to_float():
    try:
        string1 = input("enter a number: ")
        int_1 = int(string1)

        answer = float(int_1)
        print(answer)

    except ValueError:
        print("invalid input")

str_to_float()

# another way to solve this
"""
def convert(string):

    try:
        return float(string)

    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")

print(c)
"""