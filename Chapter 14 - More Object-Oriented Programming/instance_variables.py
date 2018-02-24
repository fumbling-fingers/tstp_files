# http://tinyurl.com/zmnf47e
# Instance Variables

class Rectangle():
    """Prints the length and width of rectangle objects
    we create using the Rectangle() class. In this example,
    length and width are instance variables."""

    def __init__(self, l, w):
        self.length = l         # instance variable (unique to each instance)
        self.width = w          # instance variable

    def print_size(self):
        print("This rectangle has a length of {} and a width of {}".format(self.length,self.width))

help(Rectangle)

my_rectangle = Rectangle(10,24)
my_rectangle.print_size()