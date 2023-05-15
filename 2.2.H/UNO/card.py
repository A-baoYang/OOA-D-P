"""卡牌類的類別"""
import sys

sys.path.append("..")
from CardGame.card import Card

NUMBER = list(range(10))
COLOR = ["BLUE", "RED", "YELLOW", "GREEN"]
COLOR_LOOKUP = {k: i for i, k in enumerate(COLOR)}


class UNOCard(Card):
    """類別：卡牌"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def number(self):
        """取得卡牌的 _number 屬性內容（點數）"""
        return self._number

    @property
    def color(self):
        """取得卡牌的 _color 屬性內容（花色）"""
        return self._color
