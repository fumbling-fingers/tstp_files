# Add a square_list class variable to a class called Square 
# so that every time you create a new Square object, the new 
# object gets added to the list.



class Square():

    square_list = []

    def __init__(self, s):
        self.side = s

        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.side * 4
    

square1 = Square(4)
print(Square.square_list) # prints object (or whatever __repr__ method returns)

square2 = Square(29)
print(Square.square_list) # prints object (or whatever __repr__ method returns)