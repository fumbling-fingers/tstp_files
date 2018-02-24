# when you create a class, it can inherit methods and variables from another class.
# the class that is inherited from is the 'parent class' and the class that inherits
# is the child class

# http://tinyurl.com/zrnqeo3

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("""{} by {} """.format(self.width, self.length))

# You can define a child class that inherits from a parent class by passing the name 
# of the parent class as a parameter to the child class when you create it.

class Square(Shape):
    def area(self):
        return self.width * self.length

# When a child class inherits a method from a parent class, you can override it by 
# defining a new method with the same name as the inherited method. A child class's 
# ability to change the implementation of a method inherited from its parent class 
# is called method overriding.
    def print_size(self):
        print("""I am {} by {}""".format(self.width, self.length))

# With the Shape class, you can create Shape objects with width and length. 
# In addition, Shape objects have the method print_size, which prints 
# their width and length.

my_shape = Shape(20,25)
print(my_shape.print_size())

# Because the Square class is a child class of the Shape class, it inherits the Shape 
# class's variables and methods.

my_square = Square(10,12)
print(my_square.print_size())
print(my_square.area())
