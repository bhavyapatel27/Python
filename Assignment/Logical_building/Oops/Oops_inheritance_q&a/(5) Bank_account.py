class Account:
    print("____WELCOME TO PUBLIC SMALL FINANCE BANK____\n")

    def __init__(self, account_number, account_balance):
        self.number = account_number
        self.balance = account_balance

    def deposite(self):
        pass

    def withdraw(self):
        pass


class SavingAccount(Account):
    print("__WELCOME TO YOUR SAVING ACCOUNT__\n")

    def __init__(self, account_number, account_balance, interest_rate, withdrawal_ammount, tenuar):
        super().__init__(account_number, account_balance)
        self.interest = interest_rate
        self.withdrawal = withdrawal_ammount
        self.tenuar = tenuar

    def deposite(self):
        total_balance = (self.balance * (((self.interest) / 100) * self.tenuar) + self.balance)
        print(
            f"your account number is => {self.number}\nyou have => {self.interest}% rate on your\ncurrent income => {self.balance} and\nafter => {self.tenuar} years \ntotal balance is => {total_balance}\n")

    def withdraw(self):
        left_balance = (self.balance - self.withdrawal)
        print(
            f"your account number is => {self.number}\nyou have total => {self.balance}\nin your account\nafter withdraw => {self.withdrawal} money from the nearest ATM\nnow there are => {left_balance} money left in your account\n")


print("Interest:=>\n")
person = SavingAccount(1234, 27000, 8, None, 4).deposite()
print("Withdrawal:=>\n")
person_1 = SavingAccount(1234, 3000, None, 1500, None).withdraw()


class InvestmentAccount(SavingAccount):
    print("__WELCOME TO YOUR INVESTMENT SIP ACCOUNT__\n")

    def __init__(self, account_number, account_balance, interest_rate, monthly_investment, time_period):
        super().__init__(account_number, account_balance, interest_rate, None, None)
        self.time = time_period
        self.month = monthly_investment

    def deposite(self):
        total_invested_amount = self.month * self.time
        final_benifit = total_invested_amount * (self.interest / 100) + self.balance
        print(f"You want to invest {self.month} money on each month\nwith the interest of {self.interest} per year\nfor the total {self.time} month\nso total invested amount is {total_invested_amount}\nso, your final balance including account balance after {self.time}\nis {final_benifit}")

print("Investment:=>\n")
person_1 = InvestmentAccount(7119100,5000,500,12,7).deposite()
