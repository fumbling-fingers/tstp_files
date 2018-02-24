# http://tinyurl.com/jlus42v

# moving the part of your program that collects input inside 
# of your try statement, and telling your except statement to 
# look out for two exceptions: a ZeroDivisionError and a ValueError.

try:
    a = input("type a number: ")
    b = input("type another number: ")
    a = int(a)
    b = int(b)

    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")