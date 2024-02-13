"""
Abstraction: Implement a class Animal with an abstract method speak().
Create concrete subclasses Dog, Cat, and Cow, each with their own implementation of the speak() method.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, type):
        self.type = type
    @abstractmethod
    def speak(self):
        print(f"I am a Animal")


class Dog(Animal):
    def speak(self):
        super().speak()
        speak_1 = "bark"
        print(f"and I belong from the {self.type} Category, and i speak as {speak_1}")


obj = Dog('Dog')
obj.speak()


class Cat(Animal):
    def speak(self):
        super().speak()
        speak_1 = "Meow"
        print(f"and I belong from the {self.type} Category, and i speak as {speak_1}")


obj1 = Cat('Cat')
obj1.speak()

class Cow(Animal):
    def speak(self):
        super().speak()
        speak_1 = "Moo"
        print(f"and I belong from the {self.type} Category, and i speak as {speak_1}")


obj1 = Cow('Cat')
obj1.speak()
