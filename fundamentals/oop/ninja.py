from pet import Pet, Dog

class Ninja:
    def __init__(self, firstN, lastN, pet, treats, pet_food):
        self.firstname = firstN
        self.lastname = lastN
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()




ninjaOne = Ninja("John", "Doe", Pet("Tony", "dog", "cry"),"fries", "dog food")

ninjaOne.walk()

ninjaOne.feed()

ninjaOne.bathe()


ninjaTwo = Ninja("John", "Doe", Dog(True, "Bony", "Pomeranian", "cry"),"fries", "dog food")

ninjaTwo.feed()