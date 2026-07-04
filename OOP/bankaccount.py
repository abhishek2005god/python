class bankaccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
#Deposit Function
    def deposit(self, amount):
        self.balance 