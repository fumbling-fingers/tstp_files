# write a function that takes three required parameters and two optional parameters

def add_them_up(x,y,z,a=10,b=100):

    sum = x + y + z + a + b
    print(sum)

add_them_up(3,2,1)
print("")

add_them_up(2,4,6,1,3)
print("")

add_them_up(2,1,4,5)
