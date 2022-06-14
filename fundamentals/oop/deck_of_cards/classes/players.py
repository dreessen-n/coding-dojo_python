"""Create players class"""

import classes.deck

class Players:
    """Create a model of players"""
    def __init__(self, name):
        """Initialize the attributes"""
        self.name = name
        self.hand = []

    def show_hand(self):
        """Display Hand"""
        for card in self.hand:
            card.card_info()
