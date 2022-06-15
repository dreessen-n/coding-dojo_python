import classes.ninja
import classes.pirate

michelangelo = classes.ninja.Ninja("Michelanglo")

jack_sparrow = classes.pirate.Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

print(f"Jack Sparrow's weapons:\n")
jack_sparrow.show_my_weapons()

print(f"Michelangelo's weapons:\n")
michelangelo.show_my_weapons()
