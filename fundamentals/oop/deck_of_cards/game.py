# Import shuffle from random and classes
from random import shuffle
from classes.deck import Deck
from classes.players import Players

# Create Deck of cards
bicycle = Deck()

# Shuffle the deck
bicycle.shuffle_deck()

# Print the shuffled deck
# bicycle.show_cards()

# Create computer-player
player_comp = Players('Computer')

# Create 1 players
player_1 = Players(input("What is your name: "))

# print(bicycle.show_cards())
# TODO Distribute cards to each player
for item in range(52):
    if item % 2 == 0:
        player_1.hand.append(bicycle.cards[item])
        print(player_1.hand[item].card_info())

# TODO Play game:
# game goes until one player has all the cards

# TODO rounds
"""
Each player draws top card from hand 
high card wins, winner gets card added to deck
"""

# TODO Declare the winner
