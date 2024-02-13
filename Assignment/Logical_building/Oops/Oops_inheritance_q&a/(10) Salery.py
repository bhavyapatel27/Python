class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def calculate_pay(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, id_number, hourly_rate, hours_worked):
        super().__init__(name, id_number)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, name, id_number, annual_salary):
        super().__init__(name, id_number)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 12


class ContractEmployee(Employee):
    def __init__(self, name, id_number, contract_amount):
        super().__init__(name, id_number)
        self.contract_amount = contract_amount

    def calculate_pay(self):
        return self.contract_amount


employee1 = HourlyEmployee("Bhavya", 3432, 20.00, 40)
print(f"{employee1.get_name()} (Hourly): {employee1.calculate_pay():.2f} rupees")
employee2 = SalariedEmployee("Kush", 2332, 80000)
print(f"{employee2.get_name()} (Salaried): {employee2.calculate_pay():.2f} rupees")
employee3 = ContractEmployee("Prince", 1221, 5000)
print(f"{employee3.get_name()} (Contract): {employee3.calculate_pay():.2f} rupees")
