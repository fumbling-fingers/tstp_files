# http://tinyurl.com/hlmhrwv

class AlwaysPositive():
    def __init__(self, number):
        self.n = number

    def __add__(self, other):           # overrides the default magic method __add__
        return abs(self.n + other.n)    # apply abs() to our definition of __add__
    
# When Python evaluates an expression with an addition operator, 
# it calls the method __add__ on the first operand object,
# passes the second operand object into __add__ as a parameter, 
# and returns the result.

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x.n)
print(y.n)
print(x + y) 