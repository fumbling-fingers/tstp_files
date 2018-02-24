#http://tinyurl.com/hgvnj4p

# here we are defining variables within the function (local variables)
# and as we are calling them from within that same function, we can
# still read them successfully
def f():
    x = 1
    y = 2
    z = 3
    
    print(x)
    print(y)
    print(z)

f()
