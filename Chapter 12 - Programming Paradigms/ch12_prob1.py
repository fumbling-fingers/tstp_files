# Define a class called Apple with 
# four instance variables that represent 
# four attributes of an apple.

class Apple():
    def __init__ (self, w, c, s, v):
        self.width = w
        self.color = c
        self.size = s
        self.variety = v

        print("object of class Apple has been created!")

granny_smith = Apple(2, "green", "medium", "Granny Smith")
red_delicious = Apple(1, "red", "small", "Red Delicious")
golden_delicious = Apple(1, "yellow", "small", "Golden Delicious")

print(granny_smith.color)
print(red_delicious.color)
print(golden_delicious.color)

