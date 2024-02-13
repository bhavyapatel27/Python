class Vehicle:
    def __init__(self, speed=None, color=None, year=None):
        self.speed = speed
        self.color = color
        self.year = year

    def detailsOfVehicle(self):
        pass


class Car(Vehicle):
    def __init__(self, speed, color, year):
        super().__init__(speed, color, year)

    def detailsOfVehicle(self):
        print(f"The car's speed is {self.speed} and the color is {self.color} and the year of manuf. is {self.year}")


car_1 = Car(int(input("Enter the Speed of car:\n")), input("Enter the color of the car:\n"), int(
    input("Enter the Year of Manuf.:\n")))
car_1.detailsOfVehicle()


class Bicycle(Vehicle):
    def __init__(self, speed, year):
        super().__init__(speed, None, year)

    def detailsOfVehicle(self):
        print(f"The Bicycle's speed is {self.speed} and the year of manuf. is {self.year}")


bicycle_1 = Bicycle(10, 2020)
bicycle_1.detailsOfVehicle()


class Truck(Vehicle):
    def __init__(self, speed, year, type):
        super().__init__(speed, None, year)
        self.type = type

    def detailsOfVehicle(self):
        print(
            f"The Truck's speed is {self.speed} and the year of manuf. is {self.year} also type of this truck is '{self.type}'")


truck_1 = Truck(65, 2016, 'Loaded')
truck_1.detailsOfVehicle()
