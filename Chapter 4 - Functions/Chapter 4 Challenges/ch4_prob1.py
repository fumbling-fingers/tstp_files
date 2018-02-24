# write a function that takes a number as input and returns the number squared

def square_num():
    try:
        x = input("enter a number and I will square it: ")
        int_x = int(x)

        #answer = int_x * int_x
        answer = int_x ** 2
        
        print(answer)
    
    except ValueError:
        print("invalid input.")
square_num()