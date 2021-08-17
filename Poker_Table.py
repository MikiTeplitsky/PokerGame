#   Poker Table
#
#

import Poker_Player
from Deck import *


class Poker_Table:
    # player list is by the seating of the players and will help us to know who goes next
    # or where to "put" the new player in the queue of BB/SB

    def __init__(self):
        self.deck = Deck()
        # should change by the table max player by request from server
        self.max_num_of_players = 5
        self.deck = self.deck.shuffle_deck()
        self.player_list = dict()
        for i in range(0, self.max_num_of_players):
            self.player_list[i] = None
        print(self.player_list)

    def new_game(self):
        self.deck.reset_deck()
        self.player_list.extend(self.player_list.pop())
