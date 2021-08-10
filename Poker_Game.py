#   Poker Game class
#   high card, pair, two pair, three of a kind, straight, flush, full house, four of a kind, straight flush, royal striaght flush(poker)
#

from Poker_Player import *
from Deck import *
from constants import *


class Poker_Game:

    def __init__(self, player_list):
        self.player_list = player_list
        self.table_cards = list()
        self.pot = 0

    @property
    def calculate_hand(player):
        # find functions
        value = Poker_Game.find_one_pair(player, 0)

        return 0

    def find_poker(player):

        return 0

    def find_one_pair(player, card_number):
        player_card = player.get_cards()[card_number]
        for card in Poker_Game.table_cards:
            if player_card == card:
                #  found a pair, now trying to find 3 of a kind.
                # in the 3 of a kind, we will check for 4 of a kind if we got 3
                value = ONE_PAIR
                better = Poker_Game.find_three_of_a_kind(card)
                if better != 0: value = better
        if value is None:
            player_hand = Poker_Game.find_high_cards(player)
            value = Poker_Game.sum_of_cards(player_hand)
        return value

    def find_three_of_a_kind(player_card):

        return 0

    def sum_of_cards(self, player_cards):
        sum = 0
        print(player_cards)
        for card in player_cards:
            if type(card[0]) != str: sum += card[0]
            else:
                if card[0] == 'Ace': sum += ACE
                elif card[0] == 'King': sum += KING
                elif card[0] == 'Queen': sum += QUEEN
                else: sum += JACK
        return sum