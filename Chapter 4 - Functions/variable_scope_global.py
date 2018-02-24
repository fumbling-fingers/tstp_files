#http://tinyurl.com/hgvnj4p

# here we are defining variables outside of any function (globally available)
x = 1
y = 2
z = 3

# so we will still be able to read them from within a function
def f():
    print(x)
    print(y)
    print(z)


f()
