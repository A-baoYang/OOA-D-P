"""定義玩家相關屬性與方法"""
import ast
import random
from typing import List, Union

from CardGame import Player


class Big2Player(Player):
    """繼承類別：大老二玩家"""

    def __init__(self) -> None:
        super().__init__()
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, player: "Big2Player"):
        self._next = player


class HumanPlayer(Big2Player):
    """繼承類別：真人玩家"""

    def __init__(self) -> None:
        super().__init__()

    def name_himself(self) -> None:
        name = input("Please name yourself: ")
        assert isinstance(name, str), TypeError("name 需為字串")
        self._name = name
        print(self)

    def show_card(self) -> list:
        """選擇卡牌打出"""
        card_dict = {i: c for i, c in enumerate(self._hand.cards)}
        card_indices = input(
            f"Player {self._name}:\nYou have these cards in Hand: {card_dict}\nChoose cards to show. Split with comma. Card numbers: "
        ).split(",")
        cards_to_remove = self._hand.remove_cards(
            card_indices=[int(i) for i in card_indices]
        )
        return cards_to_remove


class AIPlayer(Big2Player):
    """繼承：電腦虛擬玩家"""

    def __init__(self) -> None:
        super().__init__()

    def name_himself(self) -> None:
        self._name = f"AI #{random.randint(1, 10 ** 5)}"
        print(self)

    def show_card(self, card_choices: Union[list, None] = None) -> list:
        print(f"Player: {self._name}:\n")
        return self._hand.show_random_card(card_choices=card_choices)
