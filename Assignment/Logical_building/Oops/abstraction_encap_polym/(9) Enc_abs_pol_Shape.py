"""
Encapsulation, Abstraction & Polymorphism: Create a class Shape representing a geometric shape with attributes like color and filled (boolean).
Implement methods to calculate area and perimeter.
Subclasses like Circle and Rectangle should override these methods to provide shape-specific calculations.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color, filled):
        self._color = color
        self._filled = filled

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_filled(self, filled):
        self._filled = filled

    def get_filled(self):
        return self._filled

    @abstractmethod
    def area(self):
        return 0

    @abstractmethod
    def perimeter(self):
        return 0


class Circle(Shape):

    def __init__(self, radius, color, filled):
        super().__init__(color, filled)
        self.radius = radius

    def area(self):
        print('circle color is:', self.get_color())
        print('filled ?', self.get_filled())
        return (format(math.pi * self.radius * self.radius, '.2f'))

    def perimeter(self):
        return (format(2 * math.pi * self.radius, '.2f'))


circle = Circle(12, 'red', True)
print(circle.area())
print(circle.perimeter())


class Rectangle(Shape):

    def __init__(self, length, width, color, filled):
        super().__init__(color, filled)
        self.length = length
        self.width = width

    def area(self):
        print('rectangle color is:', self.get_color())
        print('filled ?', self.get_filled())
        return 2 * self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(12, 12, 'black', True)
print(rectangle.area())
print(rectangle.perimeter())
