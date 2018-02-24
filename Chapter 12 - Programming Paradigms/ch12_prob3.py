# Create a Triangle class with a method called area 
# that calculates and returns its area. Then create 
# a Triangle object, call area on it, and print the result.

class Triangle():
    def __init__(self, b, h):  
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height) / 2

triangle1 = Triangle(3, 4)
print("base = " + str(triangle1.base))
print("height = " + str(triangle1.height))
print("The area of the triangle is: " + str(triangle1.area()))
print("")
triangle2 = Triangle(7, 8)
print("base = " + str(triangle2.base))
print("height = " + str(triangle2.height))
print("The area of the triangle is: " + str(triangle2.area()))