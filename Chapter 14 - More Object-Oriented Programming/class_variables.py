# http://tinyurl.com/gu9unfc
# Class variables

class Rectangle():
    # docstring provides summary and expected arguments in the __init__ method
    """This class is used to calculate the   
    area of a rectangle"""
    
    recs = []       # CLASS VARIABLE - specifically a list that is shared among all 
                    # instances of the class and does not call the __init__ method
                    
    def __init__(self, w, l): 
        self.width = w              # instance variable, unique to each instance
        self.length = l             # instance variable, unique to each instance

        self.recs.append((self.width,self.length))  # create a list of tuples and append their
                                                    # width and length in the 'recs' list 

    def print_size(self):
        print("""{} by {}""".format(self.width,self.length))

# help(Rectangle)

r1 = Rectangle(11,13)

# here you are using the Class 'instance' (r1) to call the instance 'variable' (width).
print(r1.width)

# here you are using the Class 'object' (Rectangle) to call the Class 'variable' (recs[]).
# the init method is not called
r1 = Rectangle(10,24)
print (Rectangle.recs)
r2 = Rectangle(20,40)
print (Rectangle.recs)
r3 = Rectangle(100, 200)
print (Rectangle.recs)