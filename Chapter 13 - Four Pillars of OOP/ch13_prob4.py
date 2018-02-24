# 4. Create a class called Horse and a class called Rider. Use composition to model a horse that has a rider. 
# Composition models the "has a" relationship by storing an object as a variable in another object.


class Horse():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name

bella = Rider("Isabella")
padre = Horse("Padre","Mustang",bella)

print(padre.name)
print(padre.breed)
print(padre.owner)         # prints object's instance memory address
print(padre.owner.name)    # Now the Horse object 'Padre' has an owner - a Rider object named 
                            # 'Isabella' - stored in the 'owner' instance variable.
