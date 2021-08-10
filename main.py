#   Main Game

import Deck
import Poker_Table
import Poker_Player

if __name__ == '__main__':
    deck = Deck.Deck()
    deck.shuffle_deck()
    deck.print_deck()
    deck.print_next_card()
    p1 = Poker_Player.Poker_Player("miki",200)
    poker = Poker_Table.Poker_Table()
    poker.player_list[4] = p1
    for i in range(0, poker.max_num_of_players):
        if poker.player_list[i] == None:
            print(poker.player_list[i])
        else: print(poker.player_list[i].get_name())




