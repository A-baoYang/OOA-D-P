from card_pattern import Single, Pair, Straight, FullHouse, CardPattern
from typing import Callable


class CardPatternChain:
    def __init__(self) -> None:
        self.single = Single()
        self.pair = Pair()
        self.straight = Straight()
        self.fullhouse = FullHouse()

    def chain(self) -> None:
        self.single.next = self.pair
        self.pair.next = self.straight
        self.straight.next = self.fullhouse

    def add(self, pattern_name: str, pattern_cls: Callable):
        assert isinstance(pattern_cls, CardPattern), TypeError(
            "新的卡牌組合需要從 CardPattern 繼承創建"
        )
        self.pattern_name = pattern_cls()
        pt = self.single
        while pt.next:
            pt = pt.next
        pt.next = self.pattern_name
