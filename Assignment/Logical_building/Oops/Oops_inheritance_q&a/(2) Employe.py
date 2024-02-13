class Employees:
    print("=> Welcome to 'BJ Pate's Industry Salary Structure'\n")

    print("=> Currently you are in Manager's Salary:\n")

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.id = emp_id
        self.salary = salary

    def bonus(self):
        pass


class Manager(Employees):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)

    def bonus(self):
        print_bonus = (self.salary * (8.33 / 100))
        return ("{:.2f}".format(print_bonus))

    def print_details(self):
        print(
            f"name of the employee is = {self.name}\nthe id is = {self.id}\nsalary is = {self.salary}\nand total bonus is {self.bonus()}")


ob_1 = Manager(input("Enter Your Name:\n"), 200, int(input("Enter your salary:\n")))
ob_1.print_details()


class Engineer(Employees):
    print("\n=>We are now in Engineers Salary\n")

    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)

    def bonus(self):
        print_bonus = (self.salary * (8.33 / 100))
        return ("{:.2f}".format(print_bonus))

    def print_details(self):
        print(
            f"name of the employee is = {self.name}\nthe id is = {self.id}\nsalary is = {self.salary}\nand total bonus is {self.bonus()}")


ob_2 = Manager('Prince', 200, 20000)
ob_2.print_details()


class Admin_staff(Employees):
    print("\n=>We are now in Admin_staff Salary\n")

    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)

    def bonus(self):
        print_bonus = (self.salary * (8.33 / 100))
        return ("{:.2f}".format(print_bonus))

    def print_details(self):
        print(
            f"name of the employee is = {self.name}\nthe id is = {self.id}\nsalary is = {self.salary}\nand total bonus is {self.bonus()}")


ob_3 = Manager('Vaibhav', 19, 7000)
ob_3.print_details()
