# Import shuffle from random and classes
from random import shuffle
from classes.deck import Deck
import classes.players

# Create Deck of cards
bicycle = Deck()

# Shuffle the deck
bicycle.shuffle_deck()

# Divide the deck
bicycle.divide_deck()

# Print the shuffled deck
# bicycle.show_cards()

# Create computer-player
player_comp = classes.players.Players('computer')

# Create 1 players
player_1 = classes.players.Players(input("what is your name? "))

# print(bicycle.show_cards())
# TODO Distribute cards to each player
player_comp.hand = bicycle.cards_1
player_1.hand = bicycle.cards_2
player_1.hand[0].card_info()
# player_1.show_hand()

# TODO Play game:
# game goes until one player has all the cards

# TODO rounds
"""
Each player draws top card from hand 
high card wins, winner gets card added to deck
"""

# TODO Declare the winner
