#http://tinyurl.com/hgvnj4p

# here we are defining variables within the function (local variables)
def f():
    x = 1
    y = 2
    z = 3

# and are attempting to call them outside of the function
# this won't work
print(x)
print(y)
print(z)
