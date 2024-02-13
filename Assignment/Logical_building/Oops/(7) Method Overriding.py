class Shape:

    # def __init__(self):
    #     print("Hey")

    def draw(self):
        print("i'm draw")


class Circle(Shape):

    def draw(self):
        print("im draw of circle")

ob_1 = Circle()
ob_1.draw()

class Rectangle(Shape):

    def draw(self):
        print("i'm draw from Rectangle")



ob_2 = Rectangle()
ob_2.draw()
