# Encapsulation means:
# Keeping the data (variables) and the methods (functions) together inside one class 
# and protecting the data from being changed directly.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

account.deposit(1000)

account.withdraw(2000)

account.show_balance()