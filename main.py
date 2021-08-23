#   Main Game
from Poker_Table import *
from Poker_Game import *

if __name__ == '__main__':
    # nothing = ''
    deck = Deck()
    deck.shuffle_deck()
    # deck.print_deck()
    # deck.print_next_card()
    p1 = Poker_Player.Poker_Player("miki", 200)
    poker = Poker_Game(p1)
    poker.table = Poker_Table()
    poker.table.new_game()
    print(type(poker.table.deck))
    # poker.table.deck.shuffle_deck()
    # poker.table.deck.print_deck()
    # poker = Poker_Table()
    # print(poker.deck)
    # poker.deck.shuffle_deck()
    # poker.player_list[4] = p1
    # for i in range(0, poker.max_num_of_players):
    #     if poker.player_list[i] is None:
    #         print(poker.player_list[i])
    #     else: print(poker.player_list[i].get_name())
    # #
    hand = list()
    for i in range(7):
        hand.append(deck.deal_card())
    p1.hand = hand
    # print(p1.hand)
    p1.hand.sort(reverse=True)
    print(p1.hand)
    # print(p1.hand[0:5])
    # x = list(dict(p1.hand).keys())
    # print(x[0])
    # p1.hand.sort(key=lambda x:x[1][1])
    # print(p1.hand)
    # print(type(p1.hand[0][0]))
    # print(p1.hand[0][0])
    # # print(poker.sum_of_cards(p1.hand))
    # poker.new_game()
    # for i in range(0, poker.max_num_of_players):
    #     if poker.player_list[i] is None:
    #         print(poker.player_list[i])
    #     else: print(poker.player_list[i].get_name())
    # p1.hand.sort(reverse=True)
    # print(p1.hand)
    # print(p1.hand.__getitem__(0)[0])
    # hand = list()

