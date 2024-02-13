# class Parent:
#     def feature1(self):
#         print("You are accessing feature 1")
#
#     def feature2(self):
#         print("You are accessing feature 2")
#
#
# class Child(Parent):
#     def feature3(self):
#         print("You are accessing feature 3")
#
#     def feature4(self):
#         print("You are accessing feature 4")
#
# class Super(Child):
#     def feature5(self):
#         print("You are accessing feature 5")
#
# a1 = Parent()
# a2 = Child()
# a3 = Super()
#
# a1.feature1()
# a1.feature2()
# a2.feature1()
# a2.feature4()
# a3.feature1()


class Shape:
    def __init__(self, length,radius,width, pi, height):
        self.length = length
        self.radius = radius
        self.width = width
        self.pi = pi
        self.height = height
    def CircleArea(self):
        area = self.pi * self.radius * self.radius
        print(f"area of circle is : {area}")
    def RectangleArea(self):
        area = self.length * self.width * self.height
        print(f"area of rectangle is : {area}")
class Circle(Shape):
    pass
x = Circle("",12,"",3.14,"")
x.CircleArea()

class rectangle(Shape):
    pass
y = rectangle(12,"",12,"",12)
y.RectangleArea()
