"""定義抽象類別：卡牌及其他常用類別"""
from abc import ABC, abstractmethod
from typing import List
import ast
import random


class Card(ABC):
    """抽象類別：卡牌"""

    def __init__(self, **kwargs) -> None:
        for k in kwargs.keys():
            self.__setattr__(f"_{k}", kwargs[k])

    def __repr__(self) -> str:
        return f"Card({vars(self)})"


class Deck:
    """類別：牌堆"""

    def __init__(self, cards: List[Card]) -> None:
        self._all_cards = cards
        self._past_cards = []

    @property
    def cards(self):
        """取得 _all_cards 屬性內容"""
        return self._all_cards

    @cards.setter
    def cards(self, cards: List):
        self._all_cards = cards

    def size(self) -> int:
        """計算張數"""
        return len(self._all_cards)

    def shuffle(self) -> None:
        """洗牌"""
        random.shuffle(self._all_cards)

    def draw_card(self) -> Card:
        """抽牌"""
        return self._all_cards.pop()

    def collect_card(self, card: Card) -> None:
        """紀錄出過的牌"""
        self._past_cards.append(card)

    def supply_cards(self) -> None:
        """除了最新一張，將之前出過的牌重洗後加入牌堆"""
        self._all_cards.extend(random.shuffle(self._past_cards[:-1]))


class Hand:
    """類別：手牌"""

    def __init__(self) -> None:
        self._all_cards = []

    @property
    def cards(self):
        """取得 _all_cards 屬性內容"""
        return self._all_cards

    @cards.setter
    def cards(self, cards: List[Card]):
        self._all_cards = cards

    def add_cards(self, cards: List[Card]):
        """新增一些牌到手牌中"""
        self._all_cards.extend(cards)

    def size(self) -> int:
        """計算張數"""
        return len(self._all_cards)

    def remove_cards(self, card_indices: list) -> List[Card]:
        """出掉卡牌"""
        cards_to_remove = [self._all_cards[i] for i in card_indices]
        for card in cards_to_remove:
            self._all_cards.remove(card)
        print(f"Cards: {cards_to_remove} showed.")
        return cards_to_remove

    # def show_card(self) -> List[Card]:
    #     """選擇卡牌打出"""
    #     card_indices = ast.literal_eval(
    #         input(
    #             f"You have these cards in Hand: {self._all_cards}\nChoose cards to show. Card numbers: "
    #         )
    #     )
    #     cards_to_remove = self.remove_card(card_indices=card_indices)
    #     return cards_to_remove

    def show_random_card(self, card_num: int = 1) -> List[Card]:
        """隨機出牌"""
        card_indices = random.sample(range(len(self._all_cards)), card_num)
        cards_to_remove = self.remove_cards(card_indices=card_indices)
        return cards_to_remove
