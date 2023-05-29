"""定義抽象類別：玩家"""
from abc import ABC, abstractmethod


class Player(ABC):
    """抽象類別：玩家"""

    def __init__(self) -> None:
        self._name = ""
        self._hand = None

    @property
    def name(self):
        """取得玩家名稱"""
        return self._name

    @name.setter
    def name(self, name: str):
        assert isinstance(name, str), TypeError("name 需為字串")
        self._name = name

    @property
    def hand(self):
        """取得手牌"""
        return self._hand

    @hand.setter
    def hand(self, hand: "Hand"):
        self._hand = hand

    @abstractmethod
    def name_himself(self, **kwargs) -> None:
        pass

    @abstractmethod
    def show_card(self, **kwargs) -> list:
        """出牌"""

    def __repr__(self) -> str:
        return f"Player: {self._name}"
