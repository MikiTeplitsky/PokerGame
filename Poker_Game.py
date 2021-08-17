#   Poker Game class
#   high card, pair, two pair, three of a kind, straight, flush, full house,
#   four of a kind, straight flush, royal straight flush(poker)
#

from Poker_Player import *
from Deck import *
from constants import *
from Poker_Table import *


class Poker_Game:

    def __init__(self, player_list):
        self.player_list = player_list
        self.table_cards = list()
        self.table = Poker_Table()
        self.pot = 0

    def calculate_hand(self, player):
        # find functions
        best_choice = 0
        result = 0
        all_cards = self.table_cards
        all_cards.extend(player.get_cards())
        # need to sort but list sorted is not applied
        # sort_cards_by_value(all_cards)

        # check pair in hands
        # pairs from the table
        pairs_1 = self.find_pairs(player, self.table_cards, player.get_cards()[0][0])
        pairs_2 = self.find_pairs(player, self.table_cards, player.get_cards()[0][0])
        # if a better pair was found
        if (pairs_1 == ONE_PAIR and pairs_2 == THREE_OF_A_KIND) \
                or (pairs_2 == ONE_PAIR and pairs_1 == THREE_OF_A_KIND):
            best_choice = FULL_HOUSE
        if pairs_1 > best_choice:
            best_choice = pairs_1
        if pairs_2 > best_choice:
            best_choice = pairs_2
        # fins straight, flush, straight flush and royal straight flush
        straight = self.find_straight()
        flush = self.find_flush()
        # result = self.sum_of_cards(player.get_cards()) + best_choice
        return result

    # def sort_cards_by_value(self, cards):

    # sum the values of the cards - working
    def sum_of_cards(self, player_cards):
        sum_cards = 0
        for card in player_cards:
            sum_cards += card[0]
        return sum_cards

    # Let's find by the symbols of the cards
    def find_pairs(self, player, table_cards, card_number):
        player_card = player.get_cards()[card_numb]
        value = 0
        count = 0
        for card in table_cards:
            if player_card == card:
                count += 1
        if count == 1:
            value = ONE_PAIR
        elif count == 2:
            value = THREE_OF_A_KIND
        elif count == 3:
            value = FOUR_OF_A_KIND
        return value

    def find_straight(self):

        return 0

    # Let's find by the shapes of the cards
    def find_flush(self):

        return 0
