from bank import *

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.accounts = {"Account1": BankAccount(0.02,0)}



    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is Rewards Member: {self.is_rewards_member}")
        print(f"Gold points: {self.gold_card_points}")
        print("Account: ")
        for key in self.accounts.keys():
            print(key)
        return self

    def enroll(self):
        if (self.is_rewards_member == True):
            print("You are already a rewards member!")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if(self.gold_card_points >= amount):
            self.gold_card_points -= amount
            print("Transaction completed")
        else:
            print("YOU ARE BROKE MAN")
        return self
    
    def addAccount(self, accountName, interest, balance=0):
        self.accounts[accountName] = BankAccount(interest, balance)
        print(f"Updated account!")
        return self

    def make_deposit(self, accountName, amount):
        self.accounts[accountName].deposit(amount)
        return self
    
    def make_withdrawal(self, accountName, amount):
        self.accounts[accountName].withdraw(amount)
        return self
    
    def display_user_balance(self, accountName):
        print(f"{accountName}'s account info:", end=" ")
        self.accounts[accountName].display_account_info()
        return self
    
    def transfer_money(self, amount, accountName, other_user):
        self.accounts[accountName].withdraw(amount)
        print(f"{accountName}'s balance: {self.accounts[accountName].balance}")
        self.accounts[other_user].deposit(amount)
        print(f"{other_user}'s balance: {self.accounts[other_user].balance}")
        return self



kevin = User("Kevin", "Dang", "kk@gmail.com", 18)
johnny = User("Johnny", "Wheeler", "jj@yahoo.com", 27)

people = [kevin, johnny]



kevin.display_info().enroll().spend_points(50).display_info().addAccount("Credit", 0.3, 60).make_deposit("Credit",60).make_withdrawal("Credit", 20).display_user_balance("Credit")
kevin.transfer_money(50, "Credit", "Account1")
johnny.enroll().spend_points(80).display_info()
# kevin.display_info()
# kevin.enroll()
# kevin.display_info()
# kevin.spend_points(50)
# kevin.display_info()
# kevin.enroll()
# kevin.spend_points(150)
# kevin.spend_points(150)


# johnny.spend_points(80)
# johnny.enroll()

# for person in people:
#     print(person)
#     person.display_info()

