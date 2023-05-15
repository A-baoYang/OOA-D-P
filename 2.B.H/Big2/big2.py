"""賽局流程實例化"""
import sys
from player import Big2Player
from card import Big2Card
from typing import Union

sys.path.append("..")
from CardGame.cardgame import CardGame


class Big2(CardGame):
    """類別：Big2 遊戲"""

    def __init__(
        self, round_num: int = -1, draw_card_num: Union[int, None] = None, **kwargs
    ):
        super().__init__(
            game_name=kwargs["game_name"],
            cards=kwargs["cards"],
            players=kwargs["players"],
            round_num=round_num if round_num else kwargs["round_num"],
            draw_card_num=kwargs["draw_card_num"]
            if "draw_card_num" in kwargs
            else draw_card_num,
        )

        self._top_play = None
        self._top_player = None
        self._winner = None


# 新的回合由頂牌玩家開始打牌
# 直到有任一玩家將所有的手牌打完為止
