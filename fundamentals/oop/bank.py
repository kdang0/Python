class BankAccount:
    accounts = []
    def __init__(self, interest_rate, balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance < amount):
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount;
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def printInfo(cls):
        for account in cls.accounts:
            account.display_account_info


bank1 = BankAccount(0.01, 4)

bank2 = BankAccount(0.5)

bank1.deposit(50).deposit(45).deposit(56).yield_interest().display_account_info()
bank2.deposit(50).deposit(50).withdraw(20).withdraw(20).withdraw(20).withdraw(20).display_account_info()

bank1.printInfo()

