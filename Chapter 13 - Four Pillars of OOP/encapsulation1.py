# encapsulation refers to two concepts: 

# 1. objects groups variables (state) and methods (for altering state 
# or doing caculations that use state) in a singe unit

# 2. hides a class's internal data to prevent the CLIENT (code outside
# the class that uses the object) from directly accessing it

# http://tinyurl.com/j74o5rh 

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length

rectangle1 = Rectangle(4,6)
print(rectangle1.width)
print(rectangle1.length)
print(rectangle1.area())