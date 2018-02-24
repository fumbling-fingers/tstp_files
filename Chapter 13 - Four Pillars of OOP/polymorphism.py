# Polymorphism is "the ability (in programming) to present the same
# method/function for differing underlying forms (data types)." 

# http://tinyurl.com/hrxd7gn

print("Hello, World!")
print(200)
print(200.1)


# http://tinyurl.com/gnxq24x

print(type("Hello, World!"))
print(type(200))
print(type(200.1))


# You presented the same interface, the print function, for three different data types: 
# a string, an integer, and a floating-point number. You didn't have to define and call 
# three separate functions (like print_string to print strings, print_int to print integers, 
# and print_float to print floating-point numbers) to print three different data types; 
# instead, you were able to use the print function to present one interface to print them all.