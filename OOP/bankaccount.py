class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\n₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nInsufficient balance!")
        else:
            self.balance -= amount
            print(f"\n₹{amount} withdrawn successfully.")

    def show_balance(self):
        print("\n----- Account Details -----")
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# Taking input from the user
name = input("Enter your name: ")
balance = float(input("Enter your starting balance: "))

# Creating the object
acc1 = BankAccount(name, balance)

# Show current balance
acc1.show_balance()

# Deposit
deposit_amount = float(input("\nEnter amount to deposit: "))
acc1.deposit(deposit_amount)

# Show updated balance
acc1.show_balance()

# Withdraw
withdraw_amount = float(input("\nEnter amount to withdraw: "))
acc1.withdraw(withdraw_amount)

# Final balance
acc1.show_balance()