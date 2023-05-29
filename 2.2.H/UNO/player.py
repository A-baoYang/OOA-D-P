"""定義玩家相關屬性與方法"""
import ast
import random
import sys
from typing import List

sys.path.append("..")
from CardGame import Player


class UNOPlayer(Player):
    """繼承類別：UNO 玩家"""

    def __init__(self) -> None:
        super().__init__()


class HumanPlayer(UNOPlayer):
    """繼承類別：真人玩家"""

    def __init__(self) -> None:
        super().__init__()

    def name_himself(self) -> None:
        name = input("Please name yourself: ")
        assert isinstance(name, str), TypeError("name 需為字串")
        self._name = name
        print(self)

    def show_card(self) -> List["ShowdownCard"]:
        """選擇卡牌打出"""
        card_dict = {i: c for i, c in enumerate(self._hand.cards)}
        card_index = ast.literal_eval(
            input(
                f"Player {self._name}:\nYou have these cards in Hand: {card_dict}\nChoose a cards to show. Card numbers: "
            )
        )
        cards_to_remove = self._hand.remove_cards(card_indices=[card_index])
        return cards_to_remove


class AIPlayer(UNOPlayer):
    """繼承：電腦虛擬玩家"""

    def __init__(self) -> None:
        super().__init__()

    def name_himself(self) -> None:
        self._name = f"AI #{random.randint(1, 10 ** 5)}"
        print(self)

    def show_card(self) -> "ShowdownCard":
        print(f"Player: {self._name}:\n")
        return self._hand.show_random_card()
