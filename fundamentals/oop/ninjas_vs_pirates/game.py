from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

jack_sparrow.show_stats()
michelangelo.show_stats()

print("------------------------------------")
print(f"Jack Sparrow's weapons:\n")
jack_sparrow.show_my_weapons()
print("------------------------------------")

print("------------------------------------")
print(f"Michelangelo's weapons:\n")
michelangelo.show_my_weapons()
print("------------------------------------")

print("------------------------------------")
michelangelo.attack(jack_sparrow)
print("------------------------------------")
jack_sparrow.show_stats()

print("------------------------------------")
jack_sparrow.attack(michelangelo)
print("------------------------------------")
michelangelo.show_stats()
