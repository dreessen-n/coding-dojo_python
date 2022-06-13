# Pets class for Dojo Pets assginment

class Pets:
    """Model a Pet"""

    def __init__(self, name, type_of_pet, tricks, noise):
        """Initialize an instance of Pet"""
        self.name = name.title()
        self.type_of_pet = type_of_pet
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.noise = noise

    # Sleep method: increases the pet's energy by 25
    def sleep(self):
        """The pet is off to sleep"""
        print(f"Time for sleep, {self.name}!")
        # Increase pet's energy by 25
        self.energy += 25
        return self

    # Eat method: increases the pet's energy by 5 and health by 10
    def eat(self):
        """Feed the pet"""
        print(f"{self.name}, time to eat! Come and get it.")
        self.energy += 5
        self.health += 10
        return self

    # Play method: increases the pet's health by 5
    def play(self):
        """Take time to exercise and play with pet"""
        print(f"Come on {self.name}, Do you want to play?")
        self.health += 5

    # Noise method: prints out the pet's sound
    def pet_noise(self):
        """Print noise pet makes"""
        print(f"{self.noise}")

"""Create a sub class of pets for exotic pets"""

class ExoticPets(Pets):
    """Represent aspect of a Pet, specific to exoctic pets"""

    def __init__(self, name, type_of_pet, tricks, noise):
        """Initialize aspects of the parent class Pets"""
        super().__init__(name, type_of_pet, tricks, noise)

    def license(self):
        """Renew exoctic pet license"""
        print(f"Renew license for {self.name}")

# Test data below
# my_cat = Pets('fluffy', 'cat', 'none', 'Ack')
# my_cat.pet_noise()
# my_cat.play()
# my_cat.eat()
# my_cat.sleep()
# my_bird = Pets('Earl', 'raven', 'pooping', 'Caw')
# my_bird.pet_noise()
# my_bear = ExoticPets('Ben', 'bear', 'stand up', 'Aghhhhh')
# my_bear.license()
# my_bear.play()
# my_bear.pet_noise()
