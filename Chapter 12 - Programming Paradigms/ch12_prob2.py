# Create a Circle class with a method called area 
# that calculates and returns its area. Then create 
# a Circle object, call area on it, and print the 
# result. Use Python's pi function in the built-in 
# math module.

import math

class Circle():
    def __init__(self, r):
        self.radius = r 

    def area(self):
        return math.pi * (self.radius ** 2)
        
circle1 = Circle(5)
print(circle1.area())

circle2 = Circle(10)
print(circle2.area())