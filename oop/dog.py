# dog class
# from: https://realpython.com/python3-object-oriented-programming

class Dog:

    # Class/static attribute
    species = "Canis familiaris"

    # class initilizer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # convert object to a string
    def __str__(self):
        return f"{self.name} is {self.age} years old"


d1 = Dog('kaylee', 15)
print(d1)
print(d1.name)
print(d1.species)
print(d1.description())
print(d1.speak("roof"))

d2 = Dog('reilly', 2)
# print(d2)
print(d2.name)
