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
# Distribute cards to each player
player_comp.hand = bicycle.cards_1
player_1.hand = bicycle.cards_2

"""
To print out single card from hand:
player_1.hand[0].card_info()
To get the point value of card at 0 index:
player_comp.hand[0].point_val
"""

# TODO Play game:
# game goes until one player has all the cards

game = True
while game == True:

    # determine that both players still have cards
    if player_comp.hand == []:
        print(f"Game Over: {player_1.name} has won the game!")
        game = False
    if player_1.hand == []:
        print(f"Game Over: Computer has won the the game!")
        game = False

    # Print cards so we can see who has what
    print(f"Computer flips:")
    player_comp.hand[0].card_info()
    print(f"{player_1.name} flips:") 
    player_1.hand[0].card_info()

    # Find out who won
    if player_comp.hand[0].point_val == player_1.hand[0].point_val:
        print("Tie! play another round\n")
        continue
    elif player_comp.hand[0].point_val >= player_1.hand[0].point_val:
        print("Computer wins the round!\n")
        temp = player_1.hand[0]
        player_comp.hand.append(player_1.hand[0])
        del player_1.hand[0]
        print("player_1 Hand:")
        f"{player_1.show_hand()}\n"
        print("computer Hand:")
        f"{player_comp.show_hand()}\n"
    else:
        print(f"{player_1.name} wins the round!\n")
        temp = player_comp.hand[0]
        player_1.hand.append(player_comp.hand[0])
        del player_comp.hand[0]
        print("player_1 Hand:")
        f"{player_1.show_hand()}\n"
        print("computer Hand:")
        f"{player_comp.show_hand()}\n"

    game = False


# TODO rounds
"""
Each player draws top card from hand 
high card wins, winner gets card added to deck
"""

# TODO Declare the winner
