"To achieve abstraction we required encapsulation"

"Only shaw the required fields to the client, hide the process of it"

"""
Encapsulation: Create a Python class representing a car. 
Encapsulate its attributes such as make, model, and year within the class. Provide methods to get and set these attributes.
"""


class Car:
    def __init__(self):
        pass

    def set__model(self, t):
        self.__model = t

    def set__year(self, y):
        self.__year = y

    def get__model(self):
        print(self.__model)

    def get__year(self):
        print(self.__year)


ob = Car()

ob.set__model("innova")
ob.get__model()
ob.set__year(2020)
ob.get__year()
