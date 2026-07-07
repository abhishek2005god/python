#Abstraction means hiding the implementation details and showing only
#the essential features of an object.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Woof")

class Cat(Animal):

    def sound(self):
        print("Meow")

class Cow(Animal):

    def sound(self):
        print("Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()