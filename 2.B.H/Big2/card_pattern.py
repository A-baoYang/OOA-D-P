from abc import ABC, abstractmethod
from collections import Counter

import numpy as np
import logging


class CardPattern(ABC):
    def __init__(self) -> None:
        self._cards = None
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, pattern: "CardPattern"):
        self._next = pattern

    @property
    def cards(self):
        return self._cards

    @abstractmethod
    def compare(self, card_pattern: "CardPattern") -> bool:
        return True

    def __repr__(self) -> str:
        return f'{type(self).__name__}({vars(self)["_cards"]})'


class Single(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        if len(cards) == 1:
            self._cards = cards
            return self
        else:
            return self.next(cards=cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""

        assert isinstance(card_pattern, Single), TypeError("請出相同牌型 Single")

        return self._cards[0] > card_pattern.cards[0]


class Pair(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        if len(cards) == 2 and cards[0].rank == cards[1].rank:
            self._cards = cards
            return self
        else:
            return self.next(cards=cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""

        assert isinstance(card_pattern, Pair), TypeError("請出相同牌型 Pair")

        logging.info(f"{max(self._cards)} vs {max(card_pattern.cards)}")
        return max(self._cards) > max(card_pattern.cards)


class Straight(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        from card import RANK_LOOKUP

        cards = sorted(cards)
        _temp_rank = np.array([RANK_LOOKUP[card.rank] for card in cards])
        if len(cards) == 5 and all((_temp_rank[1:] - _temp_rank[:-1]) == 1):
            self._cards = cards
            return self
        else:
            return self.next(cards=cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""

        assert isinstance(card_pattern, Straight), TypeError("請出相同牌型 Straight")

        return max(self._cards) > max(card_pattern.cards)


class FullHouse(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        self._temp_rank = [card.rank for card in cards]
        if len(cards) == 5 and sorted(dict(Counter(self._temp_rank)).values()) == [
            2,
            3,
        ]:
            self._cards = cards
            return self
        else:
            raise TypeError("此次出牌未符合任何一種牌型，請重新出牌")

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""
        assert isinstance(card_pattern, FullHouse), TypeError("請出相同牌型 FullHouse")

        return self.cards[-1] > card_pattern.cards[-1]


class CardPatternHandler:
    def __init__(self) -> None:
        self.single = Single()
        self.pair = Pair()
        self.straight = Straight()
        self.fullhouse = FullHouse()

    def chain(self) -> None:
        self.single.next = self.pair
        self.pair.next = self.straight
        self.straight.next = self.fullhouse
