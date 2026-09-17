# Prerequisite: Py functions & Classes

def greet(name):
    return f"Hello, {name}"
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says woof"
    
print(greet("Rakesh"))
my_dog = Dog("Cherry",3)
print(my_dog.bark())