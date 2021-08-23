#   Poker Game class
#   high card, pair, two pair, three of a kind, straight, flush, full house,
#   four of a kind, straight flush, royal straight flush(poker)
#

from Poker_Player import *
from Deck import *
from constants import *
from Poker_Table import *


# sum the values of the cards - working
def sum_of_cards(player_cards):
    sum_cards = 0
    for card in player_cards:
        sum_cards += card[0]
    return sum_cards


def find_hand_for_two_pairs(all_cards):
    # init
    hand = list()
    extra = True
    # looking through all the cards
    for i in range(0, 7):
        # finding a pair (highest first)
        if all_cards[i][0] == all_cards[i + 1][0]:
            hand.extend([all_cards[i], all_cards[i + 1]])
            i += 1
        # if still haven't found a pair, we found our high card
        if extra is True:
            hand.extend(all_cards[i])
            extra = False
        # after we found our 5 cards, we can finish
        if len(hand) == 5:
            i = 7
    return hand


# cards are sorted
def find_hand_for_full_house(all_cards):
    # init
    hand = list()
    # looking through all the cards
    for i in range(0, 6):
        # finding a pair or a 3 of a kind
        if all_cards[i][0] == all_cards[i + 1][0]:
            hand.extend([all_cards[i][0], all_cards[i + 1][0]])
            i += 1
            if all_cards[i][0] == all_cards[i + 1][0]:
                i += 1
                hand.extend(all_cards[i][0])
        if len(hand) == 5:
            i = 7
    return hand


def find_hand_for_three_of_a_kind(all_cards):
    hand = list()
    extra = 0
    # looking through all the cards
    for i in range(0, 6):
        # found 3 of a kind
        if all_cards[i][0] == all_cards[i + 1][0]:
            hand.extend([all_cards[i], all_cards[i + 1], all_cards[i + 2][0]])
            i += 2
        # 2 high cards
        elif extra != 2:
            hand.extend(all_cards[i])
            extra += 1
        if len(hand) == 5:
            i = 7
    return hand


def find_hand_for_four_of_a_kind(all_cards):
    hand = list()
    extra = True
    for i in range(0, 6):
        if all_cards[i][0] == all_cards[i + 1][0]:
            hand.extend([all_cards[i][0], all_cards[i + 1][0], all_cards[i + 2][0], all_cards[i + 3][0]])
            i += 3
        elif extra is True:
            hand.extend(all_cards[i][0])
            extra = False
        if len(hand) == 5:
            i = 7
    return hand


# find a straight and returns if found + the cards for the straight
def find_straight(cards):
    hand = list()
    result = 0
    cards_values = list(dict(cards).keys())
    # less the 5 unique values of cards => no chance for straight
    if len(cards_values) < 5:
        return result, hand

    for i in range(0, len(cards_values) - 4):
        if cards_values[i] == (cards_values[i + 1] - 1) and cards_values[i + 1] == (cards_values[i + 2] - 1) \
                and cards_values[i + 2] == (cards_values[i + 3] - 1) and cards_values[i + 3] == (
                cards_values[i + 4] - 1):
            result = STRAIGHT

            # getting the cards to hand
            for j in range(0, 7):
                if cards[j][0] == cards_values[i]:
                    hand.extend(cards[j])
                    i += 1
                if len(hand) == 5:
                    j = 7

    # what about 5, 4, 3, 2, Ace
    if result == 0 and cards_values[0] == 14:
        for i in range(0, len(cards_values) - 4):
            if cards_values[i] == (cards_values[i + 1] - 9) and cards_values[i + 1] == (cards_values[i + 2] - 1) \
                    and cards_values[i + 2] == (cards_values[i + 3] - 1) \
                    and cards_values[i + 3] == (cards_values[i + 4] - 1):
                result = STRAIGHT

                # getting the cards to hand
                for j in range(0, 7):
                    if cards[j][0] == cards_values[i]:
                        hand.extend(cards[j])
                        i += 1
                    if len(hand) == 5:
                        j = 7

    return result, hand


# find a flush and returns if found + the cards for flush
# Heart, Spade, Club, Diamond
def find_flush(cards):
    # init
    hand = list()
    result = 0
    count_h = 0
    count_s = 0
    count_c = 0
    count_d = 0

    # find out how many we got from each shape
    for i in range(0, 6):
        if cards[i][1] == 'Heart':
            count_h += 1
        elif cards[i][1] == 'Spade':
            count_s += 1
        elif cards[i][1] == 'Club':
            count_c += 1
        else:
            count_d += 1

    # do we have a flush?
    if count_d == 5 or count_h == 5 or count_s == 5 or count_c == 5:
        result = FLUSH
        if count_d == 5:
            shape = 'Diamond'
        elif count_c == 5:
            shape = 'Club'
        elif count_s == 5:
            shape = 'Spade'
        else:
            shape = 'Heart'

        # get the hand
        for i in range(0, 7):
            if cards[i][1] == shape:
                hand.extend(cards[i][1])
            if len(hand) == 5:
                i = 7

    return result, hand


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
            if all_cards[i][0] == all_cards[i + 1][0]:
                count_pairs += 1
                if i != 4 and all_cards[i + 2][0] == all_cards[i][0]:
                    kinds = 3
                    if i != 3 and all_cards[i + 3][0] == all_cards[i][0]:
                        kinds = 4
        # 3/4 of a kind + full house
        if kinds == 3:
            # 3of a kind + full house
            if count_pairs > 1:
                best_choice = FULL_HOUSE
                hand = find_hand_for_full_house(all_cards)
            else:
                best_choice = THREE_OF_A_KIND
                hand = find_hand_for_three_of_a_kind(all_cards)
        # 4 of a kind
        elif kinds == 4:
            best_choice = FOUR_OF_A_KIND
            hand = find_hand_for_four_of_a_kind(all_cards)

        # finds straight
        straight, hand_straight = find_straight(all_cards)

        # finds flush
        flush, hand_flush = find_flush(all_cards)

        # flush or straight
        if flush != 0 or straight != 0:
            # straight + flush
            if flush != 0 and straight != 0 and (hand_flush == hand_straight):
                hand = hand_straight
                # if the second highest card is a king then we got a royal straight flush
                if hand[1][0] == 13:
                    best_choice = POKER
                else:
                    # straight flush
                    best_choice = STRAIGHT_FLUSH
            # flush
            elif best_choice < flush:
                best_choice = FLUSH
                hand = hand_flush

            # straight
            elif best_choice < STRAIGHT:
                best_choice = STRAIGHT
                hand = hand_straight

        if best_choice == 0:
            hand = all_cards[0:5]

        return sum_of_cards(hand) + best_choice
