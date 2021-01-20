class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, deposit_amount):
        self.balance = deposit_amount + self.balance 
        print("You have deposited ${}. Your new balance is ${}".format(deposit_amount, self.balance))
        
    def withdraw(self, withdraw_amount):
        if withdraw_amount >= self.balance:
            print("Funds unavailable.")
        else:
            self.balance = self.balance - withdraw_amount
            print("You have withdrawn ${}. Your new balance is ${}".format(withdraw_amount, self.balance))
            
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

# acct1 = Account('Jose',100)

# print(acct1)

# acct1.owner

# acct1.balance

# acct1.deposit(50)

# acct1.withdraw(75)

# acct1.withdraw(500)