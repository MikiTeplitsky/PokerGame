#   Poker Game class
#   high card, pair, two pair, three of a kind, straight, flush, full house, four of a kind, straight flush, royal striaght flush(poker)
#

import Poker_Player
import Deck
import constants

class Poker_Game:

    def __init__(self,player_list):
        self.player_list = player_list
        self.deck = Deck.Deck()
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
        player_card =  player.get_cards()[card_number]
        for card in Poker_Game.table_cards:
            if player_card == card:
                value = constants.ONE_PAIR
                Poker_Game.find_three_of_a_kind(card):

        return 0

    def find_three_of_a_kind(player_card):

        return 0