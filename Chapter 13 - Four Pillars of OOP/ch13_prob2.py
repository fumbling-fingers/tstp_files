# 2. Define a method in your Square class called change_size 
# that allows you to pass in a number that increases or decreases 
# (if the number is negative) each side of a Square object by 
# that number.



class Square:
    def __init__(self, s):      # initialize a new object of the 'Square' class
        self.side = s           # pass the argument
        
    def calculate_perimeter(self):      # pass the object and it's variable
        return self.side * 4            # carry out arithmetic on variable

    def change_size(self, s):      # pass object and new variable
        self.side += s


square1 = Square(4)

print(square1.side)
print(square1.calculate_perimeter())

square1.change_size(8)

print(square1.side)
print(square1.calculate_perimeter())

square1.change_size(-6)

print(square1.side)
print(square1.calculate_perimeter())
