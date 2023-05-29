from itertools import product
from CardGame import Deck
from collections import Counter
from itertools import combinations
import sys

sys.path.append("..")
from Big2.card import Big2Card, Big2Hand, RANK, SUIT

cards = [Big2Card(rank=item[0], suit=item[1]) for item in product(RANK, SUIT)]
deck = Deck(cards=cards)
deck.shuffle()

hand = Big2Hand()
for i in range(13):
    hand.add_cards([deck.draw_card()])

hand.cards


def _card_combinations(_all_cards, r, rank_collect):
    collect = {}
    for rank in rank_collect:
        c = list(
            combinations(
                iterable=[
                    {k: card} for k, card in _all_cards.items() if card.rank == rank
                ],
                r=r,
            )
        )
        c = [list(item) for item in c]
        collect[rank] = c
    return collect


_all_cards = {k: v for k, v in enumerate(sorted(deck.cards))}
card_in_rank = [card.rank for card in _all_cards.values()]
card_stats = dict(Counter(card_in_rank))

rank_in_pair = [rank for rank, count in card_stats.items() if count >= 2]
pairs = _card_combinations(_all_cards=_all_cards, r=2, rank_collect=rank_in_pair)
rank_in_triple = [rank for rank, count in card_stats.items() if count >= 3]
triples = _card_combinations(
    _all_cards=_all_cards,
    r=3,
    rank_collect=rank_in_triple,
)
