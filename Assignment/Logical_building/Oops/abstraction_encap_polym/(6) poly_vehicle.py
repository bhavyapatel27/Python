"""
 Polymorphism: Create a base class called Vehicle with a method drive().
 Implement subclasses Car, Truck, and Motorcycle, each with its own drive() method.
 Use polymorphism to call the appropriate drive() method based on the type of vehicle.
"""

class Vehicle:

    def drive(self):
        pass

class Car:

    def drive(self):
        print("Hii I'm Driving a car")

class Truck:
    def drive(self):
        print("Hey !! There i'm Driving a loaded truck")

class Motorcycle:
    def drive(self):
        print("Heyaa !! fuel of my Motorcycle is over :( ")

Car_obj = Car()
Truck_obj = Truck()
Mc_obj = Motorcycle()

for i in (Car_obj, Truck_obj, Mc_obj):
    i.drive()