from .weapons import Weapons

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.weapons = [
            {'sword': Weapons('sword', 3, 3)},
            {'gun': Weapons('gun', 5, 3)}
        ]

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def show_my_weapons(self):
        for weapon in self.weapons:
            for key, value in weapon.items():
                print(f"weapon: {key}\n")
                print(f"Strength Damage: {value.strength_damage_pts}\n")
                print(f"Health Damage: {value.health_damage_pts}\n")
