# http://tinyurl.com/hockur5
import time

# Don't use variables defined in a try statement in an except statement, 
# because an exception could occur before the variable is defined, and 
# an exception will get raised inside of your except statement when you 
# try to use it.


try:
    b = "no errors, yet" # variable defined in a try statement
    10/0
    c = "I will never get defined." # variable defined in a try statement
except ZeroDivisionError:
    print(b)
    time.sleep(2)
    print(c)  # exception is raised inside of your except statement
              # because 'c' was never defined