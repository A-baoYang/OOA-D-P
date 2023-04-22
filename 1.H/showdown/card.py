"""docstring"""
from itertools import product
import random
from typing import List

from player import Player

RANK = [str(i) for i in list(range(2, 11))] + ["J", "Q", "K", "A"]
RANK_LOOKUP = {k: i for i, k in enumerate(RANK)}
SUIT = ["CLUB", "DIAMOND", "HEART", "SPADE"]
SUIT_LOOKUP = {k: i for i, k in enumerate(SUIT)}


class Deck:
    """docstring"""

    def __init__(self) -> None:
        self._cards = [Card(*item) for item in product(RANK, SUIT)]

    @property
    def cards(self):
        """docstring"""
        return self._cards

    @cards.setter
    def cards(self, cards: List):
        """docstring"""
        self._cards = cards

    def shuffle(self) -> None:
        """docstring"""
        random.shuffle(self._cards)

    def drawcard(self, player: Player) -> None:
        """docstring"""
        player.add_cards_to_hand([self._cards.pop()])


class Card:
    """docstring"""

    def __init__(self, rank: str, suit: str) -> None:
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """docstring"""
        return self._rank

    @property
    def suit(self):
        """docstring"""
        return self._suit

    def __repr__(self) -> str:
        return f"Card(Rank={self._rank}, Suit={self._suit})"


class Hand:
    """docstring"""

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._all_cards = []

    @property
    def all_cards(self):
        """docstring"""
        return self._all_cards

    @all_cards.setter
    def all_cards(self, cards: List[Card]):
        self._all_cards = cards

    def add_cards(self, cards: List[Card]):
        """docstring"""
        self._all_cards += cards

    def get_hand_size(self) -> int:
        """docstring"""
        return len(self._all_cards)

    def show_card(self, card_index: int) -> Card:
        """docstring"""
        removed_card = self._all_cards[card_index]
        print(f"{removed_card} showed.")
        self._all_cards.remove(removed_card)
        return removed_card

    def show_random_card(self):
        """docstring"""
        card_index = random.randint(0, len(self._all_cards) - 1)
        return self.show_card(card_index)


class HandExchange:
    """docstring"""

    def __init__(self, keep_rounds: int) -> None:
        self.exchange_records = {}
        self.keep_rounds = keep_rounds

    def exchange(
        self, source_player: Player, target_player: Player, start_round: int
    ) -> None:
        """docstring"""
        print(
            f"Hand Exchang happened at round {start_round}, from {source_player} "
            f"to {target_player}."
        )
        source_player.hand, target_player.hand = (
            target_player.hand,
            source_player.hand,
        )
        source_player.is_exchanged_hand = True
        self.exchange_records.update(
            {
                source_player.name: {
                    "target_player": target_player,
                    "start_round": start_round,
                    "rest_rounds": self.keep_rounds,
                }
            }
        )

    def countdown(self) -> None:
        """docstring"""
        for record in self.exchange_records.values():
            if record["rest_rounds"] > 0:
                record["rest_rounds"] -= 1
