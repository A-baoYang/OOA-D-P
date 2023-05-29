from itertools import product

from card import RANK, SUIT, Big2Card, Big2Hand
from player import AIPlayer, HumanPlayer, PlayerChain
from big2 import Big2

from card_pattern import CardPatternHandler
from CardGame import CardGame, Card


cards = [Big2Card(rank=item[0], suit=item[1]) for item in product(RANK, SUIT)]
players = [HumanPlayer() for i in range(4)]
big2 = Big2(game_name="test_Big2", cards=cards, players=players)
big2.prerequisite()
# big2._player_chain = PlayerChain(players=big2._players)
# big2._deck.shuffle()
# draw_card_num = big2._deck.size() // len(big2._players)
# for i, player in big2._players.items():
#     player.name_himself()
#     player.hand = Big2Hand()
#     player.hand.add_cards([big2._deck.draw_card() for i in range(draw_card_num)])
big2.decide_first_player()
big2._top_player.hand.cards
