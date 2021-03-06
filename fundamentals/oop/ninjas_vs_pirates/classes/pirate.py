from .weapons import Weapons

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.weapons = [
            {'sword': Weapons('sword', 3, 3)},
            {'gun': Weapons('gun', 5, 3)},
        ]

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        """Attack with a weapon"""
        print(f"{self.name} ATTACKS!")
        print("Choose your weapon:")
        attack_weapon = input("Enter: 'sword' or 'gun': ")
        if attack_weapon == 'sword':
            ninja.health -= self.weapons[0]['sword'].health_damage_pts
            ninja.strength -= self.weapons[0]['sword'].strength_damage_pts
        else:
            ninja.health -= self.weapons[1]['gun'].health_damage_pts
            ninja.strength -= self.weapons[1]['gun'].strength_damage_pts
        return self

    def show_my_weapons(self):
        """Display list of weapons for ninja"""
        for weapon in self.weapons:
            for key, value in weapon.items():
                print(f"weapon: {key}")
                print(f"Strength Damage: {value.strength_damage_pts} Health Damage: {value.health_damage_pts}\n")
