# Create Rectangle and Square classes with a method 
# called calculate_perimeter that calculates the 
# perimeter of the shapes they represent. Create 
# Rectangle and Square objects and call the method 
# on both of them.

class Rectangle:
    def __init__(self, w, l):   # initialize new object of the 'Rectangle' class passing arguments
        self.width = w          # assign first argument to 'w'
        self.length = l         # assign second argument to 'l'

    def calculate_perimeter(self):                      # pass the object and it's variables
        return (self.width * 2) + (self.length * 2)     # carry out arithmetic on variables


class Square:
    def __init__(self, s):      # initialize a new object of the 'Square' class
        self.side = s           # pass the argument
        
    def calculate_perimeter(self):      # pass the object and it's variable
        return self.side * 4            # carry out arithmetic on variable

    def change_size(self, s):      # pass object and new variable
        self.side = s

rectangle1 = Rectangle(4,6)
square1 = Square(3)
square2 = Square(4)
square3 = square2



print("Rectangle object created with length of {} and width of {}".format(rectangle1.length,rectangle1.width))
print("has a perimeter of {}".format(rectangle1.calculate_perimeter()))
print("")


print("Square Object ONE was created with a side the length of {}.".format(square1.side))
print("has a perimeter of {}".format(square1.calculate_perimeter()))


print("")
print("Square Object TWO was created with side of {}".format(square2.side))
print("")
square2.change_size(6)
print("But using the 'change_size()' function, the side length of Square Object TWO was changed to {}".format(square2.side))
print("producing a square object with a perimeter of {}".format(square2.calculate_perimeter()))


print("")
print("Square Object THREE was created with side of {}".format(square3.side))
print("")
square3.change_size(9)
print("But using the 'change_size()' function, the side length of Square Object TWO was changed to {}".format(square3.side))
print("producing a square object with a perimeter of {}".format(square3.calculate_perimeter()))