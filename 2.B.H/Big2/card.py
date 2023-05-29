"""卡牌類的類別"""
from collections import Counter
from itertools import combinations
from typing import Union
from CardGame import Card, Hand


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

        from card_pattern import CardPatternHandler

        # 每位玩家有自己的 CardPatternHandler
        self._card_pattern_handler = CardPatternHandler()
        self._card_pattern_handler.chain()

    def is_contains_club_3(self, cards: Union[list, None] = None):
        if cards is None:
            cards = self.cards
        if [c for c in cards if c.rank == "3" and c.suit == "C"]:
            return True
        return False

    def _card_combinations(self, _all_cards, r, rank_collect):
        collect = []
        for rank in rank_collect:
            c = list(
                combinations(
                    iterable=[
                        {k: card} for k, card in _all_cards.items() if card.rank == rank
                    ],
                    r=r,
                )
            )
            c = [list(item) for item in c]
            collect += c
        return collect

    def pattern_detection(self):
        # self._all_cards 改成 dict 會比較方便(可以提供編號出去)
        _all_cards = {k: v for k, v in enumerate(sorted(self._all_cards))}
        card_in_rank = [card.rank for card in _all_cards.values()]
        card_stats = dict(Counter(card_in_rank))

        # pair
        rank_in_pair = [rank for rank, count in card_stats.items() if count >= 2]
        self.pairs = self._card_combinations(
            _all_cards=_all_cards, r=2, rank_collect=rank_in_pair
        )

        # fullhouse
        rank_in_triple = [rank for rank, count in card_stats.items() if count >= 3]
        self.triples = self._card_combinations(
            _all_cards=_all_cards,
            r=3,
            rank_collect=rank_in_triple,
        )
        if (not rank_in_triple) or (
            len(rank_in_pair) <= 1 and len(rank_in_triple) <= 1
        ):
            self.fullhouse = []
        else:
            for rank in rank_in_triple:
                _fh = []
                # 從 pairs 和 triples 組出所有 fullhouse 組合

        # straight
        self.straight = []
        card_id_in_rank = {i: v for i, v in enumerate(card_in_rank)}
        sorted_card_id_in_rank = {
            i: v for i, v in sorted(card_id_in_rank.items(), key=lambda item: item[1])
        }
        ## 2 pointers
        i = j = 0
        prev_rank = list(sorted_card_id_in_rank.values())[0]
        for card_id, card_rank in sorted_card_id_in_rank.items():
            if card_id == 0:
                pass
            else:
                if card_rank == prev_rank + 1:
                    j += 1
                else:
                    i = j + 1
                    j = i
            if j - i + 1 == 5:
                self.straight.append(
                    [sorted_card_id_in_rank[card_id] for card_id in range(i, j + 1)]
                )
                i = j + 1
                j = i
