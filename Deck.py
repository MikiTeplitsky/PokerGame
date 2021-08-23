#   Deck of cards class
#   4 types of shapes: Spade, Heart, Diamond & Club
#   13 types of symbols: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King

from itertools import product
import random


class Deck:
    deck = list()

    def __init__(self):
        deck = self.deck.extend(list((product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))))
        # deck = self.deck.extend(
        #     list((product(["Ace", "Jack", "Queen", "King"], ['Spade', 'Heart', 'Diamond', 'Club']))))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        print(self.deck)

    # help function
    def print_next_card(self):
        card = self.deck.pop()
        print("{} of {}".format(card[0], card[1]))

    def deal_card(self):
        return self.deck.pop(0)

    # not sure
    def reset_deck(self):
        del self.deck
        self.deck = Deck()
        self.deck.shuffle_deck()
