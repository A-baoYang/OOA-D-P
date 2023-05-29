from abc import ABC, abstractmethod
from collections import Counter
from itertools import combinations, product
from typing import Union, Callable
import numpy as np
import logging


class CardPattern(ABC):
    def __init__(self) -> None:
        self._cards = None
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, pattern: "CardPattern"):
        self._next = pattern

    @property
    def cards(self):
        return self._cards

    @abstractmethod
    def compare(self, card_pattern: "CardPattern") -> bool:
        return True

    @abstractmethod
    def _compare(self, cards: list) -> bool:
        return True

    @abstractmethod
    def detect(self, **kwargs) -> list:
        return []

    def _filter(
        self,
        cards: list,
        is_compare: bool = False,
        constraint_func: Union[Callable, None] = None,
    ) -> list:
        logging.info(constraint_func)
        qualified = []
        for c_dict in cards:
            _c_dict_cards = list(c_dict.values())
            if is_compare and constraint_func:
                if not self._compare(cards=_c_dict_cards) and constraint_func(
                    _c_dict_cards
                ):
                    qualified.append(c_dict)
            elif not is_compare and constraint_func:
                if constraint_func(_c_dict_cards):
                    qualified.append(c_dict)
            elif is_compare and not constraint_func:
                if not self._compare(cards=_c_dict_cards):
                    qualified.append(c_dict)
            else:
                qualified.append(c_dict)
        return qualified

    def __repr__(self) -> str:
        return f'{type(self).__name__}({vars(self)["_cards"]})'


class Single(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        if len(cards) == 1:
            self._cards = cards
            return self
        else:
            return self.next(cards=cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""

        assert isinstance(card_pattern, Single), TypeError("請出相同牌型 Single")

        return self._cards[0] > card_pattern.cards[0]

    def _compare(self, cards: list) -> bool:
        return self._cards[0] > cards[0]

    def detect(
        self,
        _hand: "Hand",
        is_compare: bool,
        constraint_func: Union[Callable, None] = None,
    ) -> list:
        """從手牌中列出符合 Single 且符合條件的出牌組合"""

        _single_cards = [{k: v} for k, v in _hand._all_cards_dict.items()]
        logging.info(f"_single_cards: {_single_cards}")
        qualified = self._filter(
            cards=_single_cards, is_compare=is_compare, constraint_func=constraint_func
        )
        logging.info(f"qualfied: {qualified}")
        return [list(card_set.keys()) for card_set in qualified]


class Pair(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        if len(cards) == 2 and cards[0].rank == cards[1].rank:
            self._cards = cards
            return self
        else:
            return self.next(cards=cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""

        assert isinstance(card_pattern, Pair), TypeError("請出相同牌型 Pair")

        return max(self._cards) > max(card_pattern.cards)

    def _compare(self, cards: list) -> bool:
        return max(self._cards) > max(cards)

    def detect(
        self,
        _hand: "Hand",
        is_compare: bool,
        constraint_func: Union[Callable, None] = None,
    ) -> dict:
        """從手牌中列出符合 Pair 且符合條件的出牌組合"""
        _rank_in_pair = [
            rank for rank, count in _hand._card_stats.items() if count >= 2
        ]
        _pairs_dict = get_card_combinations(
            cards=_hand._all_cards_dict, r=2, rank_collect=_rank_in_pair
        )
        _pairs_cards = []
        for v in _pairs_dict.values():
            _pairs_cards += v
        qualified = self._filter(
            cards=_pairs_cards, is_compare=is_compare, constraint_func=constraint_func
        )
        logging.info(f"qualfied: {qualified}")
        return [list(card_set.keys()) for card_set in qualified]


class Straight(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        from card import RANK_LOOKUP

        cards = sorted(cards)
        _temp_rank = np.array([RANK_LOOKUP[card.rank] for card in cards])
        if len(cards) == 5 and all((_temp_rank[1:] - _temp_rank[:-1]) == 1):
            self._cards = cards
            return self
        else:
            return self.next(cards=cards)

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""

        assert isinstance(card_pattern, Straight), TypeError("請出相同牌型 Straight")

        return max(self._cards) > max(card_pattern.cards)

    def _compare(self, cards: list) -> bool:
        return max(self._cards) > max(cards)

    def detect(
        self,
        _hand: "Hand",
        is_compare: bool,
        constraint_func: Union[Callable, None] = None,
    ) -> dict:
        """從手牌中列出符合 Straight 且符合條件的出牌組合"""
        from card import RANK_LOOKUP, RANK

        straights, _straight_ids = [], []
        unique_sorted_rank = []
        for c in _hand._all_cards_dict.values():
            if RANK_LOOKUP[c.rank] not in unique_sorted_rank:
                unique_sorted_rank.append(RANK_LOOKUP[c.rank])

        for i in range(5, len(unique_sorted_rank) + 1):
            _temp_rank = np.array(unique_sorted_rank[i - 5 : i])
            if all((_temp_rank[1:] - _temp_rank[:-1]) == 1):
                _straight_ids.append(_temp_rank.tolist())

        for id_set in _straight_ids:
            straights += list(
                product(
                    *[
                        [
                            {k: v}
                            for k, v in _hand._all_cards_dict.items()
                            if v.rank == RANK[r]
                        ]
                        for r in id_set
                    ]
                )
            )
        _straights_cards = escape_list_of_dict(data=straights)
        qualified = self._filter(
            cards=_straights_cards,
            is_compare=is_compare,
            constraint_func=constraint_func,
        )
        logging.info(f"qualfied: {qualified}")
        return [list(card_set.keys()) for card_set in qualified]


class FullHouse(CardPattern):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, cards: list) -> None:
        self._temp_rank = [card.rank for card in cards]
        if len(cards) == 5 and sorted(dict(Counter(self._temp_rank)).values()) == [
            2,
            3,
        ]:
            self._cards = cards
            return self
        else:
            raise TypeError("此次出牌未符合任何一種牌型，請重新出牌")

    def compare(self, card_pattern: CardPattern) -> bool:
        """設定大小判斷依據"""
        assert isinstance(card_pattern, FullHouse), TypeError("請出相同牌型 FullHouse")

        return self.cards[-1] > card_pattern.cards[-1]

    def _compare(self, cards: list) -> bool:
        return self.cards[-1] > cards[-1]

    def detect(
        self,
        _hand: "Hand",
        is_compare: bool,
        constraint_func: Union[Callable, None] = None,
    ) -> dict:
        """從手牌中列出符合 Straight 且符合條件的出牌組合"""

        _rank_in_pair = [
            rank for rank, count in _hand._card_stats.items() if count >= 2
        ]
        _pairs_dict = get_card_combinations(
            cards=_hand._all_cards_dict, r=2, rank_collect=_rank_in_pair
        )
        _rank_in_triple = [
            rank for rank, count in _hand._card_stats.items() if count >= 3
        ]
        _triples_dict = get_card_combinations(
            cards=_hand._all_cards_dict,
            r=3,
            rank_collect=_rank_in_triple,
        )
        fullhouses, _fullhouse_ids = [], []
        # 從 _pairs_dict 和 _triples_dict 組出所有 fullhouse 組合
        fh_pair_rank = set(_rank_in_pair) - set(_rank_in_triple)
        if _rank_in_triple and fh_pair_rank:
            for rank_tri in _rank_in_triple:
                _fullhouse_ids += [
                    {"triplet": item[0], "pair": item[1]}
                    for item in product(
                        [rank_tri], [r for r in _rank_in_pair if r != rank_tri]
                    )
                ]
            for fh in _fullhouse_ids:
                fullhouses += [
                    dict(list(item[0].items()) + list(item[1].items()))
                    for item in list(
                        product(_triples_dict[fh["triplet"]], _pairs_dict[fh["pair"]])
                    )
                ]
            qualified = self._filter(
                cards=fullhouses, is_compare=is_compare, constraint_func=constraint_func
            )
            logging.info(f"qualfied: {qualified}")
            return [list(card_set.keys()) for card_set in qualified]
        else:
            return []


def get_card_combinations(cards, r, rank_collect) -> dict:
    collect = {}
    for rank in rank_collect:
        c = list(
            combinations(
                iterable=[{k: card} for k, card in cards.items() if card.rank == rank],
                r=r,
            )
        )
        c = escape_list_of_dict(data=c)
        collect[rank] = c
    return collect


def escape_list_of_dict(data: list) -> list:
    _c = []
    for item in data:
        __c = {}
        for _item in item:
            __c.update(_item)
        _c.append(__c)
    return _c


def get_id_from_combinations(data: dict) -> list:
    combination_ids = []
    for v in data.values():
        combination_ids += [list(_v.keys()) for _v in v]
    return combination_ids


def get_cards_from_combinations(data: dict) -> list:
    combination_cards = []
    for v in data.values():
        combination_cards += [list(_v.values()) for _v in v]
    return combination_cards
