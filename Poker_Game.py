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
        # find 1 pair, 3 of a kind, 4 of a kind
        value1 = self.find_pairs(player, self.table_cards, player.get_cards[0])
        if value1 != FOUR_OF_A_KIND:
            # no need to check if its 4 of a kind
            value2 = self.find_pairs(player, self.table_cards, player.get_cards[1])
        else:
            #  adding the highest card we can get
            value2 = self.choose_high_card_value(player, self.table_cards)
        # straight + flush
        if value1 + value2 == 0:
            values, type_of_straight = self.find_straight()
            if values == 0:
                values = self.find_flush()
                if values == 0:
                    # need to find the highest cards values
                    exit()
            else:
                if self.find_flush() != 0:
                    if type_of_straight == 'Royal':
                        values = POKER
                    else:
                        values = STRAIGHT_FLUSH
        else:
            values = value1 + value2
        return values

    # sum the values of the cards - working
    def sum_of_cards(self, player_cards):
        sum_cards = 0
        for card in player_cards:
            sum_cards += card[0]
        return sum_cards

    # Let's find by the symbols of the cards
    def find_pairs(self, player, table_cards, card_number):
        player_card = player.get_cards()[card_number]
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

    def choose_high_card_value(self, player, table_card):
        player_hand = player.get_cards()
        card_value = player_hand[0][0]
        for card in table_card:
            if card[0] > card_value:
                card_value = card[0]
        if card_value < player_hand[1][0]:
            card_value = player_hand[1][0]
        return card_value

    def find_straight(self):
        type_of_straight = ''

        return 0, type_of_straight

    # Let's find by the shapes of the cards
    def find_flush(self):

        return 0
