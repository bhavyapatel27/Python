class Student:
    def __init__(self):
        self.__name = ''
        self.__age = 0
        self.__grade = ''

    def StudentDetail(self):
        print(self.__name + " age is: " + str(self.__age) + " and his grade is: " + self.__grade)

    def set__name(self, name):
        self.__name = name

    def get__name(self):
        print(self.__name)

    def set__age(self, a):
        self.__age = a

    def get__age(self):
        print(self.__age)

    def set__grade(self, b):
        self.__grade = b

    def get__grade(self):
        print(self.__grade)


ob = Student()
ob.set__name("Bhavya")
ob.get__name()
ob.set__age(20)
ob.get__age()
ob.set__grade("A")
ob.get__grade()
ob.StudentDetail()
