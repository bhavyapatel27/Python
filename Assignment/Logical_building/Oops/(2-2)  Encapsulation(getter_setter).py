class Student:
    def __init__(self):
        self.name = "Bhavya"
        self.__city = "Pa"

    def StudentDetail(self):
        print(self.name + " : " + self.__city)

    def set__city(self, t):
        self.__city = t

    def get__city(self):
        print(self.__city)


ob = Student()

ob.set__city("Ahmedabad")
"if i comment uper line then i'll get a Pa as a city"
ob.StudentDetail()

"to access or to know the private variable value:"
ob.get__city()
