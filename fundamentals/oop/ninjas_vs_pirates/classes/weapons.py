# Create weapons class

class Weapons:
    """Model weapons for battle use"""
    # Make a list of all weapons
    all_weapons = []

    def __init__(self, weapon_type, health_damage_pts, strength_damage_pts):
        self.weapon_type = weapon_type
        self.health_damage_pts = health_damage_pts
        self.strength_damage_pts = strength_damage_pts
        Weapons.all_weapons.append(self)

    def show_weapons(self):
        """Display arsenal of weapons"""
        print(f"weapon: {self.weapon_type}\nStrength Damage: {self.strength_damage_pts}\nHealth Damage: {self.health_damage_pts}")
