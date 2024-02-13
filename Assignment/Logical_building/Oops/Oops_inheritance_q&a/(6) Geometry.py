import math


class Shape:

    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Sphere(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class Cube(Shape):

    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def area(self):
        return 6 * self.side_length ** 2

    def volume(self):
        return self.side_length ** 3

rectangle = Rectangle(4, 3)
print(f"Rectangle area: {rectangle.area()}")
sphere = Sphere(2)
print(f"Sphere area: {sphere.area()}")
cube = Cube(5)
print(f"Cube area: {cube.area()}")
