# Make a Hexagon class with a method called calculate_perimeter 
# that calculates and returns its perimeter. Then create a 
# Hexagon object, call calculate_perimeter on it, and print the result.

class Hexagon():
   def __init__(self, s1, s2, s3, s4, s5, s6):
       self.side1 = s1
       self.side2 = s2
       self.side3 = s3
       self.side4 = s4
       self.side5 = s5
       self.side6 = s6

   def perimeter(self):
       return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon1 = Hexagon(2, 2, 2, 2, 2, 2)
print(hexagon1.perimeter())
print("")
hexagon2 = Hexagon(2, 3, 4, 5, 6, 7)
print(hexagon2.perimeter())
