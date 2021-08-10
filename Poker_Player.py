#   Poker Player class
#
#   What he needs:
#   1. Hand
#   2. credit

from Deck import *
from constants import *

class Poker_Player:
# credit need to change to the minimum buy-in of the table or the amount the player want 'till max table buy-in

    def __init__(self, nick ,buy_in):
        self.credit = buy_in
        self.hand = list()
        self.name = nick
    
    def reset_hand(self):
        hand = list()
        
    def get_card(self, deck):
        self.hand.extend(deck.deal_card())

    def get_credit(self, amount):
        self.credit += amount

    def bet(self, amount):
        self.credit -= amount

    def get_cards(self):
        return self.hand

    def get_name(self):
        return self.name

    def set_name(self, nick):
        self.name = nick
