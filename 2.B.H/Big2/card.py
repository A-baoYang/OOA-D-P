"""卡牌類的類別"""
from collections import Counter
from typing import Union
from CardGame import Card, Hand
import random


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

    def __repr__(self) -> str:
        return f"{self._suit}[{self._rank}]"


class Big2Hand(Hand):
    def __init__(self) -> None:
        super().__init__()

        from card_pattern_handler import CardPatternHandler

        # 每位玩家有自己的 CardPatternHandler
        self._card_pattern_handler = CardPatternHandler()
        self._card_pattern_handler.chain()

    def arrange_cards(self) -> None:
        """整理手牌的動作"""
        self.cards.sort()
        self._all_cards_dict = {k: v for k, v in enumerate(sorted(self.cards))}
        self._card_stats = dict(
            Counter([card.rank for card in self._all_cards_dict.values()])
        )

    def is_contains_club_3(self, cards: Union[list, None] = None) -> bool:
        """手牌/出牌是否包含梅花 3"""
        if cards is None:
            cards = self.cards
        if [c for c in cards if c.rank == "3" and c.suit == "C"]:
            return True
        return False

    def show_random_pattern(
        self,
        hand: "Hand",
        top_play: Union["CardPattern", None] = None,
        is_first_round: bool = False,
    ) -> "CardPattern":
        """執行合法隨機出牌"""
        from card_pattern import Single, Pair, Straight, FullHouse

        self.arrange_cards()
        constraint_func = self.is_contains_club_3 if is_first_round else None
        if top_play:
            return top_play.detect(_hand=hand, is_compare=True)
        else:
            _single = self._card_pattern_handler.single(
                cards=[Big2Card(rank="A", suit="S")]
            )
            _pair = self._card_pattern_handler.pair(
                cards=[Big2Card(rank="A", suit="S"), Big2Card(rank="A", suit="D")]
            )
            _straight = self._card_pattern_handler.straight(
                cards=[
                    Big2Card(rank="10", suit="S"),
                    Big2Card(rank="J", suit="H"),
                    Big2Card(rank="Q", suit="S"),
                    Big2Card(rank="K", suit="H"),
                    Big2Card(rank="A", suit="S"),
                ]
            )
            _fullhouse = self._card_pattern_handler.fullhouse(
                cards=[
                    Big2Card(rank="K", suit="D"),
                    Big2Card(rank="K", suit="S"),
                    Big2Card(rank="A", suit="D"),
                    Big2Card(rank="A", suit="S"),
                    Big2Card(rank="A", suit="C"),
                ]
            )
            pattern_type = random.choice([_single, _pair, _straight, _fullhouse])
            # pattern_type = _single
            return pattern_type.detect(
                _hand=hand, is_compare=False, constraint_func=constraint_func
            )
