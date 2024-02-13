"""
2. Encapsulation: Define a class called BankAccount that encapsulates an account balance.
Implement methods to deposit and withdraw money, ensuring that the balance cannot be accessed directly from outside the class.
"""


class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(100)
account.deposit(50)
account.withdraw(25)

# print(account.__balance)

print(account.get_balance())
