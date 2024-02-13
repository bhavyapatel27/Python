"""Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data."""

# to define a private member prefix the member name with double underscore “__”.

#Normal Program to access the variable

# class Student:
#     def __init__(self):
#         self.name = "Bhavya"
#         self.school = "Shantiniketan"
#
#     def combine(self):
#         return self.name + self.school
#
# patan_school = Student()
# print(patan_school.name)
# print(patan_school.school)
# print(patan_school.combine())

#private variable

# class Student:
#     def __init__(self):
#         self.name = "Bhavya"
#         self.__school = "Shantiniketan"
#
#     def combine(self):
#         return self.name + self.__school
#
# patan_school = Student()
# print(patan_school.name)
# print(patan_school.__school)
# print(patan_school.combine())
#

'''error: Student' object has no attribute 'school'......But it have attribute student so we can't access it'''

#Access private variable

class Student:
    def __init__(self):
        self.name = "Bhavya"
        self.__school = "Shantiniketan" #private variable we can't access it outside the class

    def combine(self):
        return self.name + self.__school

patan_school = Student()
print(patan_school.name)
print(patan_school._Student__school) #we are accessing by declaring class inside a object
#accessing private variable
print(patan_school.combine())

"""As mentioned in a upper it's called as a name handling to access the private variable"""