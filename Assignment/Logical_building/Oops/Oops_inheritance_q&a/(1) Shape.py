import math


class Shape:
    def __init__(self, radius=None, length=None, width=None):
        self.radius = radius
        self.length = length
        self.width = width

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, None, None)

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


ob_1 = Circle(2)
print("area of circle is:", ob_1.calculate_area())

ob_2 = Circle(5)
print("paremeter of circle is:", ob_2.calculate_perimeter())


class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__(None, length, width)

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


ob_3 = Rectangle(12, 34)
print("area of ractangle is:", ob_1.calculate_area())

ob_4 = Rectangle(3.14, 5)
print("perimeter of ractangle is:", ob_2.calculate_perimeter())


class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.base + self.side1 + self.side2


triangle = Triangle(3, 4, 5, 5)
print("Triangle area:", triangle.calculate_area())
print("Triangle perimeter:", triangle.calculate_perimeter())
