class Food:
    def __init__(self, name, type, taste):
        self.name = name
        self.type = type
        self.taste = taste

    def healthy(self):
        print(f"the {self.name} is a type of {self.type} and it taste's like a {self.taste}")


class Fruits(Food):
    def __init__(self, name, type, taste, caleries):
        super().__init__(name, type, taste)
        self.caleries = caleries

    def healthy(self):
        super().healthy()
        print(f"it has a {self.caleries} Kcal")


apple = Fruits('apple', 'fruits', 'sour', '0.095')
apple.healthy()


class Vegetables(Fruits):
    def __init__(self, name, type, taste, caleries):
        super().__init__(name, type, taste, caleries)

    def healthy(self):
        super().healthy()
        # print(f"it has a {self.caleries} Kcal")


cocumber = Vegetables('Cocumber', 'Veg', 'sweet', '0.045')
cocumber.healthy()
