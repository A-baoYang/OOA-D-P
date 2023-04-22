"""docstring"""
from abc import ABC, abstractmethod
from typing import List
import random


class Player(ABC):
    """docstring"""

    def __init__(self) -> None:

        from card import Hand

        self._point = 0
        self._is_exchanged_hand = False
        self._hand = Hand(owner="")

    @property
    def name(self):
        """docstring"""
        return self._name

    @name.setter
    def name(self, newname: str):
        self._name = newname
        self._hand.owner = self._name

    @property
    def hand(self):
        """docstring"""
        return self._hand

    @hand.setter
    def hand(self, hand: "Hand"):
        self._hand = hand

    @property
    def point(self):
        """docstring"""
        return self._point

    @point.setter
    def point(self, point: int):
        self._point = point

    @property
    def is_exchanged_hand(self):
        """docstring"""
        return self._is_exchanged_hand

    @is_exchanged_hand.setter
    def is_exchanged_hand(self, is_exchanged_hand: bool):
        self._is_exchanged_hand = is_exchanged_hand

    @abstractmethod
    def showcard(self):
        """docstring"""

    @abstractmethod
    def decide_exchange(self, **kwargs):
        """docstring"""

    def add_cards_to_hand(self, cards: List) -> None:
        """docstring"""
        self._hand.add_cards(cards)

    def gain_points(self, points: int) -> None:
        """docstring"""
        self._point += points

    def __repr__(self) -> str:
        return f"Player: {self._name}"


class HumanPlayer(Player):
    """docstring"""

    def __init__(self) -> None:
        super().__init__()

        self._name = input("Enter player name: ")
        self._hand.owner = self._name

    def showcard(self):

        print({i: c for i, c in enumerate(self._hand.all_cards)})
        card_index = int(
            input(f"Player {self._name}:\nChoose card to show. Card number: ")
        )
        return self._hand.show_card(card_index=card_index)

    def decide_exchange(self, **kwargs) -> List:
        players = kwargs["players"]
        is_exchange = input(
            f"Player {self._name}:\nDo you want to exchange hand card this round? (Y/N)"
        )
        if is_exchange == "Y":
            is_exchange = 1
            print({i: p for i, p in enumerate(players)})
            exchange_player = players[
                int(
                    input(
                        f"Player {self._name}:\nWho do you wanna exchange with? Please enter player number: "
                    )
                )
            ]
        else:
            is_exchange, exchange_player = 0, None

        return [is_exchange, exchange_player]


class AIPlayer(Player):
    """docstring"""

    def __init__(self) -> None:
        super().__init__()

        self._name = f"AI Player #{random.randint(1, 10 ** 5)}"

    def showcard(self):
        return self._hand.show_random_card()

    def decide_exchange(self, **kwargs) -> List:
        players, round_num = kwargs["players"], kwargs["round_num"]
        is_exchange = random.choices(
            [0, 1], [0.5 + 1 / round_num, 0.5 - 1 / round_num]
        )[0]
        exchange_player = random.choice(players)
        return [is_exchange, exchange_player]
