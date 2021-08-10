#   Main Game

from Deck import *
from Poker_Table import *
from Poker_Player import *
from Poker_Game import *

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle_deck()
    # deck.print_deck()
    # deck.print_next_card()
    p1 = Poker_Player("miki",200)
    poker = Poker_Game(p1)
    # poker = Poker_Table()
    # poker.player_list[4] = p1
    # for i in range(0, poker.max_num_of_players):
    #     if poker.player_list[i] == None:
    #         print(poker.player_list[i])
    #     else: print(poker.player_list[i].get_name())

    hand = list()
    for i in range(5):
        # print(deck.deal_card())
        hand.append(deck.deal_card())
    p1.hand = hand
    # print(p1.hand)
    # print(type(p1.hand[0][0]))
    # print(p1.hand[0][0])
    print(poker.sum_of_cards(p1.hand))



