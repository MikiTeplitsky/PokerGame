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
        hand = list()
        best_choice = 0

        # all cards
        all_cards = self.table_cards
        all_cards.extend(player.get_cards())

        # sort by value
        all_cards.sort(reverse=True)

        # check pairs and three/four of a kind
        count_pairs = 0
        kinds = 0
        for i in range(0, 7):
            if all_cards[i][0] == all_cards[i+1][0]:
                count_pairs += 1
                if i != 4 and all_cards[i+2][0] == all_cards[i][0]:
                    kinds = 3
                    if i != 3 and all_cards[i+3][0] == all_cards[i][0]:
                        kinds = 4

        if kinds == 3:
            if count_pairs > 1:
                best_choice = FULL_HOUSE
                hand = self.find_hand_for_full_house(all_cards)
            else:
                best_choice = THREE_OF_A_KIND
                hand = self.find_hand_for_three_of_a_kind(all_cards)

        elif kinds == 4:
            best_choice = FOUR_OF_A_KIND
            hand = self.find_hand_for_four_of_a_kind(all_cards)


        # finds straight
        straight, hand_straight = self.find_straight(all_cards)

        # finds flush
        flush, hand_flush = self.find_flush()

        # flush or straight
        if flush != 0 or straight != 0:
            # straight + flush
            if flush != 0 and straight != 0:
                # royal straight flush
                # need to check if its the same cards
                if hand[0] == 14:
                    best_choice = POKER
                else:
                    # straight flush
                    best_choice = STRAIGHT_FLUSH
                    hand = self.find_hand_for_straight_flush()
            # flush
            elif best_choice < flush:
                best_choice = FLUSH
                hand = hand_flush

            # straight
            elif best_choice < STRAIGHT:
                best_choice = STRAIGHT
                hand = hand_straight

        return self.sum_of_cards(hand) + best_choice

    # sum the values of the cards - working
    def sum_of_cards(self, player_cards):
        sum_cards = 0
        for card in player_cards:
            sum_cards += card[0]
        return sum_cards

    # Let's find by the symbols of the cards
    def find_one_pair(self, player, table_cards, card_number):
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

    # find a straight and returns if found + the cards for the straight
    def find_straight(self):

        return 0

    # find a flush and returns if found + the cards for flush
    def find_flush(self):

        return 0

    # cards are sorted
    def find_hand_for_full_house(self, all_cards):
        # init
        hand = list()
        # looking through all the cards
        for i in range(0, 7):
            # finding a pair or a 3 of a kind
            if all_cards[i][0] == all_cards[i + 1][0]:
                hand.extend([all_cards[i], all_cards[i + 1]])
                # trying to look if its the 3 of a kind
                if i != 6 and all_cards[i] == all_cards[i + 2]:
                    hand.extend(all_cards[i + 2])
        return hand

    # cards are sorted
    def find_hand_for_two_pairs(self, all_cards):
        # init
        hand = list()
        pair = 0
        # looking through all the cards
        for i in range(0, 7):
            # finding a pair (highest first)
            if all_cards[i][0] == all_cards[i + 1][0]:
                hand.extend([all_cards[i], all_cards[i + 1]])
                pair += 1
                i += 2
            # if still haven't found a pair, we found our high card
            if pair == 0:
                hand.extend(all_cards[i])
            # after we found our 5 cards, we can finish
            if len(hand) == 5:
                i = 7
        return hand

    def find_hand_for_straight_flush(self, all_cards):

        pass
