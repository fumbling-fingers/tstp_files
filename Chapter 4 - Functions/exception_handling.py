# http://tinyurl.com/jcg5qwp

# this program will still fail if you enter a string
a = input("type a number: ")
b = input("type another number: ")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("you cannot divide by zero.")