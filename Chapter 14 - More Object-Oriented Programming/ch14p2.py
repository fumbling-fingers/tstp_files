# Change the Square class so that when you print a Square object, 
# a message prints telling you the len of each of the four sides 
# of the shape. For example, if you create a square with Square(29) 
# and print it, Python should print 29 by 29 by 29 by 29.


class Square():

    square_list = []

    def __init__(self, s):
        self.side = s

        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.side * 4

    # Python calls a magic method called __repr__ it inherited from 
    # Object on it, and prints whatever the __repr__ method returns. 
    # You can override the inherited __repr__ method to change what
    # prints, like we are doing here:

    def __repr__(self):     
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)


square1 = Square(4)
print(Square.square_list) # calls __repr__ function

square2 = Square(13)
print(Square.square_list) # calls __repr__ function