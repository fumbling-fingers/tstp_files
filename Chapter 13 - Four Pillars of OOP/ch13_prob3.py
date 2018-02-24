# 3. Create a class called Shape. Define a method in it 
# called what_am_i that prints "I am a shape" when called. 
# Change your Square and Rectangle classes from the 
# previous challenges to inherit from Shape, create 
# Square and Rectangle objects, and call the new method 
# on both of them.

class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)


class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

# QUESTION
# why does using the print() function 
# produce 'none' in the output
#
# ANSWER
# It's the return value of the function, which you print out. 
# If there is no return statement (or just a return without an 
# argument), an implicit return None is added to the end of a 
# function.
#
# You probably want to return the values in the function instead of printing them:
rectangle1 = Rectangle(3,2)
print(rectangle1.calculate_perimeter()) 
print(rectangle1.what_am_i())           # print will return 'none'
print("----")

square1 = Square(4)                     
print(square1.calculate_perimeter())
square1.what_am_i()                     # here we are not using print, but implicitly
                                        # using the 'return()' function