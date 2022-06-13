"""Create players class"""

import classes.deck

class Players:
    """Create a model of players"""
    def __init__(self, name):
        """Initialize the attributes"""
        self.name = name
        self.hand = []

    def __repr__(self):
        display = f"{self.string_val} of {self.suit} : {self.point_val} points"
        return display

    def show_hand(self):
        """Display Hand"""
        for card in self.hand:
            card.card_info()
