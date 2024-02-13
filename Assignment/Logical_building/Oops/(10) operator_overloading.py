class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


"If anyone calls + to Vector we need to call __add__ That is operator overloading"


def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)


def __mul__(self, other):
    return Vector(self.x * other, self.y * other)


def __str__(self):
    return f"({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(2, 1)

v3 = v1 + v2  # if we didn't define __add__ then we can not perform add operation
print(v3)

v4 = v1 * 2
print(v4)
