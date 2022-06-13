# Ninjas class for Dojo Pets assignment
"""Create a class for Ninjas"""

# Import in Pets class
import pets

class Ninjas:
    """Model a ninja student"""

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        """Initialize the ninja class"""
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pets.Pets('Earl', 'bird', 'pooping on people', 'Caw')
        self.treats = treats
        self.pet_food = pet_food

    def __repr__(self):
        """__repr__ is used to format class print to terminal"""
        display = f"ninja: {self.first_name} {self.last_name}, pet: {self.pet.name}, {self.pet.name} likes {self.treats} for treats, and eats {self.pet_food} for food"
        return display

# Walk method: walks the ninja's pet invoking the pet play() method
    def walk(self):
        """Walk the pet"""
        ninja_neal.pet.play()

# Feed method: feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        """Feed the pet"""
        ninja_neal.pet.eat()

# Bath method: cleans the ninja's pet invoking the pet noise() mehtod
    def bathe(self):
        """Bathe the pet"""
        ninja_neal.pet.pet_noise()

ninja_neal = Ninjas('neal', 'dreessen', 'bird', 'meat fat', 'trash')
print(ninja_neal)
ninja_neal.feed()
ninja_neal.walk()
ninja_neal.bathe()

"""
SENSEI BONUS: use inheritance to create a sub class of Pets
Created a sub class called ExoticPets
"""
# I got this working as a sub class in the Pets Class file but not here... yet!



