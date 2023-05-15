"""卡牌類的類別"""
from abc import ABC, abstractmethod
from collections import Counter
import sys

sys.path.append("..")
from CardGame.card import Card

RANK = [str(i) for i in list(range(3, 11))] + ["J", "Q", "K", "A", "2"]
RANK_LOOKUP = {k: i for i, k in enumerate(RANK)}
SUIT = ["C", "D", "H", "S"]  # 梅花, 方塊, 愛心, 黑桃
SUIT_LOOKUP = {k: i for i, k in enumerate(SUIT)}


class Big2Card(Card):
    """類別：卡牌"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def rank(self):
        """取得卡牌的 _rank 屬性內容（點數）"""
        return self._rank

    @property
    def suit(self):
        """取得卡牌的 _suit 屬性內容（花色）"""
        return self._suit

    def __gt__(self, card: "Big2Card"):
        """設定大小判斷依據"""
        if RANK_LOOKUP[self._rank] > RANK_LOOKUP[card.rank]:
            return True
        elif (RANK_LOOKUP[self._rank] == RANK_LOOKUP[card.rank]) and (
            SUIT_LOOKUP[self._suit] > SUIT_LOOKUP[card.suit]
        ):
            return True
        return False


class CardPattern(ABC):
    def __init__(self, cards: list) -> None:
        self.cards = cards

    @abstractmethod
    def compare(self, card_pattern: "CardPattern") -> bool:
        return True


class Single(CardPattern):
    def __init__(self, cards: list) -> None:
        super().__init__(cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""
        return self.cards[0].compare(card_pattern=card_pattern.cards[0])


class Pair(CardPattern):
    def __init__(self, cards: list) -> None:
        super().__init__(cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""
        return max(self.cards).compare(card_pattern=max(card_pattern.cards))


class Straight(CardPattern):
    def __init__(self, cards: list) -> None:
        super().__init__(cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""
        return max(self.cards).compare(card_pattern=max(card_pattern.cards))


class FullHouse(CardPattern):
    def __init__(self, cards: list) -> None:
        super().__init__(cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""
        dict(Counter(self.cards))
        return max(self.cards).compare(card_pattern=max(card_pattern.cards))
