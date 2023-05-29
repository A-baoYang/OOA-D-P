"""定義玩家相關屬性與方法"""
import ast
import random
import sys
from abc import abstractmethod
from typing import List

sys.path.append("..")
from CardGame.player import Player


class ShowdownPlayer(Player):
    """繼承類別：Showdown 玩家"""

    def __init__(self) -> None:
        super().__init__()

        self._point = 0
        self._is_exchanged_hand = False

    @property
    def point(self):
        """取得玩家點數"""
        return self._point

    @point.setter
    def point(self, point: int):
        self._point = point

    @property
    def is_exchanged_hand(self):
        """取得玩家是否已經交換過手牌"""
        return self._is_exchanged_hand

    @is_exchanged_hand.setter
    def is_exchanged_hand(self, is_exchanged_hand: bool):
        self._is_exchanged_hand = is_exchanged_hand

    @abstractmethod
    def decide_exchange(self, **kwargs):
        """決定是否交換手牌"""

    def gain_points(self, points: int) -> None:
        """計入當回合得分"""
        self._point += points

    def __repr__(self) -> str:
        return super().__repr__()


class HumanPlayer(ShowdownPlayer):
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


class AIPlayer(ShowdownPlayer):
    """繼承：電腦虛擬玩家"""

    def __init__(self) -> None:
        super().__init__()

    def name_himself(self) -> None:
        self._name = f"AI Player #{random.randint(1, 10 ** 5)}"
        print(self)

    def show_card(self) -> "ShowdownCard":
        return self._hand.show_random_card()

    def decide_exchange(self, **kwargs) -> List:
        players, round_num = kwargs["players"], kwargs["round_num"]
        is_exchange = random.choices(
            [0, 1], [0.5 + 1 / round_num, 0.5 - 1 / round_num]
        )[0]
        exchange_player = random.choice(players)
        return [is_exchange, exchange_player]
