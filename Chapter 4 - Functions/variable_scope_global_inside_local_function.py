#http://tinyurl.com/zclmda7

# You can WRITE to a global variable from anywhere, but WRITING to
# a global variable inside of a local scope takes an extra step.
# You must explicitly use the global keyword, followed by the
# variable you want to change.


x = 100

def f():
    global x
    x += 1
    print(x)

f()


# Without scope, you could access every variable anywhere in your program,
# which would be problematic.

