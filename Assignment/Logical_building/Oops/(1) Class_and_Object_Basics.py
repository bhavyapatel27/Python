class Car:
    def __init__(self, name, model, color, owner):
        self.name = name
        self.model = model
        self.color = color
        self.owner = owner

    def features(self):
        print(f"{self.name} is {self.model} model with {self.color} color and it's {self.owner}'s car")

spiny = Car("Spiny", 2023, "Red", "Bhavya")
spiny.features()

cars24_name = input("Enter Your Car Name:\n")
cars24_model = int(input("Enter the Model Year:\n"))
cars24_color = input("Enter the Car Color:\n")
cars24_owner = input("Enter, which owner is this car:\n")

cars24 = Car(cars24_name, cars24_model, cars24_color, cars24_owner)
cars24.features()
