"""
 Abstraction: Create an abstract class called Shape with an abstract method area(). Implement concrete subclasses Circle and Rectangle.
 Each subclass should override the area() method to calculate the area of the respective shape.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        print(format(math.pi * self.radius * self.radius,".2f"))


circle = Circle()
circle.area(2)


class Rectangle(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        print(self.length * self.width)


rectangle = Rectangle()
rectangle.area(2, 2)
