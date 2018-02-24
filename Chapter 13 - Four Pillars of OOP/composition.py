# http://tinyurl.com/zqg488n

class Dog():
    def __init__ (self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

# when you create a 'Dog' object you pass in a 'Person' object
# as the owner PARAMETER

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick) # <- pass 'Person' object as owner PARAMETER

print(stan.owner.name)
