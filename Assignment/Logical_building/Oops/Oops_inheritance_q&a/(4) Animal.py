class Animal:
    def __init__(self, color=None, legs=None, name=None, speed=None, type=None):
        self.color_of_animal = color
        self.no_of_legs = legs
        self.name_of_animal = name
        self.speed_of_animal = speed
        self.type_of_animal = type

    def PrintDetailsOfAnimal(self):
        pass


class Mamal(Animal):
    def __init__(self, legs, name, type, birth):
        super().__init__(None, legs, name, None, type)
        self.birth = birth

    def PrintDetailsOfAnimal(self):
        print(
            f"legs={self.no_of_legs}, name={self.name_of_animal}, type={self.type_of_animal}, giving new life by={self.birth}")


animal = Mamal(4, 'elephant', 'mamal', 'birth')
animal.PrintDetailsOfAnimal()


class Bird(Animal):
    def __init__(self, color, legs, name, speed, type, birth):
        super().__init__(color, legs, name, speed, type)
        self.birth = birth

    def PrintDetailsOfAnimal(self):
        print(
            f"color={self.color_of_animal}, legs={self.no_of_legs}, name={self.name_of_animal}, type={self.type_of_animal}, speed={self.speed_of_animal}, giving new life by={self.birth}")


bird = Bird('blue', 2, 'peacock', 35, 'bird', 'eggs')
bird.PrintDetailsOfAnimal()


class Fish(Animal):
    def __init__(self, name, speed, type, birth):
        super().__init__(None, None, name, speed, type)
        self.birth = birth

    def PrintDetailsOfAnimal(self):
        print(
            f"name={self.name_of_animal}, type={self.type_of_animal}, speed={self.speed_of_animal}, giving new life by={self.birth}")


Fish = Fish('Shark','45','fish','eggs')
Fish.PrintDetailsOfAnimal()
