from .weapons import Weapons


class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.weapons = [
            {'katana': Weapons('katana', 4, 3)},
            {'tanto': Weapons('tanto', 2, 1)},
        ]
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        """Attack with a weapon"""
        print(f"{self.name} ATTACKS!")
        print("Choose your weapon:")
        attack_weapon = input("Enter: 'katana' or 'tanto': ")
        if attack_weapon == 'katana':
            pirate.health -= self.weapons[0]['katana'].health_damage_pts
            pirate.strength -= self.weapons[0]['katana'].strength_damage_pts
        else:
            pirate.health -= self.weapons[1]['tanto'].health_damage_pts
            pirate.strength -= self.weapons[1]['tanto'].strength_damage_pts
        return self

    def show_my_weapons(self):
        """Display list of weapons for ninja"""
        for weapon in self.weapons:
            for key, value in weapon.items():
                print(f"weapon: {key}")
                print(f"Strength Damage: {value.strength_damage_pts} Health Damage: {value.health_damage_pts}\n")
                
