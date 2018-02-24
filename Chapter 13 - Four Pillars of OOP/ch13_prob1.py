# Create Rectangle and Square classes with a method 
# called calculate_perimeter that calculates the 
# perimeter of the shapes they represent. Create 
# Rectangle and Square objects and call the method 
# on both of them.

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)


class Square:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

rectangle1 = Rectangle(4,6)
square1 = Square(3)

print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())