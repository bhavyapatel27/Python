"""Encapsulation & Polymorphism: Design a class Employee with encapsulated attributes like name, salary, and role.
Implement a method calculate_bonus() that calculates a bonus based on the employee's role.
Subclasses like Manager and Developer should override this method to provide role-specific bonus calculations."""


class Employee:
    def __init__(self, name, salary, role):
        self._name = name
        self._salary = salary
        self._role = role

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_role(self, role):
        self._role = role

    def get_role(self):
        return self._role

    def calculate_bonus(self):
        return 0


class Manager(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.2


class Developer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.08


name_input = input("Enter the name: ")
salary_input = int(input("Enter the Salary: "))

if salary_input > 20000:
    manager = Manager(name_input, salary_input, 'Manager')
    print('Bonus will be__:', manager.calculate_bonus())
else :
    developer = Developer(name_input, salary_input, 'Developer')
    print('Developer bonus', developer.calculate_bonus())


