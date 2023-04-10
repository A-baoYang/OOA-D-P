from itertools import product
import random


RANK = [str(i) for i in list(range(2, 11))] + ["J", "Q", "K", "A"]
RANK_LOOKUP = {k: i for i, k in enumerate(RANK)}
SUIT = ["CLUB", "DIAMOND", "HEART", "SPADE"]
SUIT_LOOKUP = {k: i for i, k in enumerate(SUIT)}


class Deck:
    def __init__(self) -> None:
        self._cards = [Card(*item) for item in product(RANK, SUIT)]
        
    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def drawcard(self, player) -> None:
        self._random_card = self._cards.pop()
        player.add_cards_to_hand([self._random_card])


class Card:
    def __init__(self, rank, suit) -> None:
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        return f"Card(Rank={self._rank}, Suit={self._suit})"


class Hand:
    def __init__(self, owner) -> None:
        self.owner = owner
        self._all_cards = []

    def get_hand_size(self) -> int:
        return len(self._all_cards)

    def show_player_cards(self):
        print(f"Player {self.owner} has these cards: {self._all_cards}")

    def show_random_card(self):
        card = random.choice(self._all_cards)
        self._all_cards.remove(card)
        return card