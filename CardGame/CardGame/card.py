"""定義抽象類別：卡牌及其他常用類別"""
import random
from abc import ABC
from typing import Union
import logging


class Card(ABC):
    """抽象類別：卡牌"""

    def __init__(self, **kwargs) -> None:
        for k in kwargs.keys():
            self.__setattr__(f"_{k}", kwargs[k])

    def __repr__(self) -> str:
        return f"Card({vars(self)})"


class Deck:
    """類別：牌堆"""

    def __init__(self, cards: list) -> None:
        self._all_cards = cards
        self._past_cards = []

    @property
    def cards(self):
        """取得 _all_cards 屬性內容"""
        return self._all_cards

    @cards.setter
    def cards(self, cards: list):
        self._all_cards = cards

    def size(self) -> int:
        """計算張數"""
        return len(self.cards)

    def shuffle(self) -> None:
        """洗牌"""
        logging.info("Shuffling Deck...")
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """抽牌"""
        return self.cards.pop()

    def collect_card(self, card: Card) -> None:
        """紀錄出過的牌"""
        self._past_cards.append(card)

    def supply_cards(self) -> None:
        """除了最新一張，將之前出過的牌重洗後加入牌堆"""
        self.cards.extend(random.shuffle(self._past_cards[:-1]))


class Hand:
    """類別：手牌"""

    def __init__(self) -> None:
        self._all_cards = []

    @property
    def cards(self):
        """取得 _all_cards 屬性內容"""
        return self._all_cards

    @cards.setter
    def cards(self, cards: list):
        self._all_cards = cards

    def add_cards(self, cards: list):
        """新增一些牌到手牌中"""
        self.cards.extend(cards)
        self.arrange_cards()

    def size(self) -> int:
        """計算張數"""
        return len(self.cards)

    def get_cards(self, card_indices: list) -> list:
        """出示卡牌"""
        self.arrange_cards()
        return [self.cards[i] for i in card_indices]

    def arrange_cards(self) -> None:
        """整理手牌的動作"""
        self.cards.sort()

    def remove_cards(
        self,
        cards_to_remove: Union[list, None] = None,
        card_indices: Union[list, None] = None,
    ) -> list:
        """出掉卡牌"""
        cards_to_remove = (
            cards_to_remove
            if cards_to_remove
            else self.get_cards(card_indices=card_indices)
        )
        self.arrange_cards()
        for card in cards_to_remove:
            self.cards.remove(card)
        logging.info(f"Cards: {cards_to_remove} showed.")
        return cards_to_remove

    def show_random_card(
        self, card_num: int = 1, card_choices: Union[list, None] = None
    ) -> list:
        """隨機出牌"""
        if card_choices is not None:
            card_indices = random.choice(card_choices)
        else:
            card_indices = random.sample(range(len(self.cards)), card_num)
        return card_indices
