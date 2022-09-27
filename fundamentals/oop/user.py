class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if (self.is_rewards_member == True):
            print("You are already a rewards member!")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if(self.gold_card_points >= amount):
            self.gold_card_points -= amount
            print("Transaction completed")
        else:
            print("YOU ARE BROKE MAN")


kevin = User("Kevin", "Dang", "kk@gmail.com", 18)
johnny = User("Johnny", "Wheeler", "jj@yahoo.com", 27)

people = [kevin, johnny]




kevin.display_info()
kevin.enroll()
kevin.display_info()
kevin.spend_points(50)
kevin.display_info()
kevin.enroll()
kevin.spend_points(150)
kevin.spend_points(150)


johnny.spend_points(80)
johnny.enroll()

for person in people:
    print(person)
    person.display_info()

