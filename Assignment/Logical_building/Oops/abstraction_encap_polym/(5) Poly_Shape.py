"""
Polymorphism: Define a function calculate_area() that accepts any object representing a shape (e.g., Circle or Rectangle) and
returns its area. This function should demonstrate polymorphism in action.
"""
import math


class Shape:
    def calculate_area(self):
        pass


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print("area of circle is:", format(math.pi * self.radius * self.radius, ".2f"))


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print("area of rectangle is:", self.length * self.width)


obj = Circle(12)
obj1 = Rectangle(12, 12)

for i in (obj, obj1):
    i.calculate_area()
