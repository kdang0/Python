
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100 

    
    def sleep(self):
        print(f"{self.name} is slep")
        self.energy += 25

    def eat(self):
        print(f"{self.name} is eat")
        self.energy += 5
        self.health += 10

    def play(self):
        print(f"{self.name} is play")
        self.health += 5

    def noise(self):
        print(f"{self.name} is noise")
        print("ASDHASDKJA")

class Dog(Pet):
    def __init__(self, dances, name, type, tricks):
        self.dances = dances
        super().__init__(name, type, tricks)

    def eat(self):
        super().eat()
        print("AHAHAHAHAHA INHERITANCE")
