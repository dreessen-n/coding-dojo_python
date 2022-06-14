from . import card
from random import shuffle

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []
        self.cards_1 = []
        self.cards_2 = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def shuffle_deck(self):
        """Shuffle the deck before distributing cards"""
        shuffle(self.cards)
        
    def divide_deck(self):
        """Split the deck between two list"""
        self.cards_1 = self.cards[:27]
        self.cards_2 = self.cards[27:]

