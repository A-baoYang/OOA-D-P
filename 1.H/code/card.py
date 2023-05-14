"""卡牌類的類別"""
from itertools import product
import random
from typing import List

from player import Player

RANK = [str(i) for i in list(range(2, 11))] + ["J", "Q", "K", "A"]
RANK_LOOKUP = {k: i for i, k in enumerate(RANK)}
SUIT = ["CLUB", "DIAMOND", "HEART", "SPADE"]
SUIT_LOOKUP = {k: i for i, k in enumerate(SUIT)}


class Deck:
    """類別：牌堆"""

    def __init__(self) -> None:
        self._cards = [Card(*item) for item in product(RANK, SUIT)]

    @property
    def cards(self):
        """取得 _cards 屬性內容"""
        return self._cards

    @cards.setter
    def cards(self, cards: List):
        self._cards = cards

    def shuffle(self) -> None:
        """洗牌"""
        random.shuffle(self._cards)

    def drawcard(self, player: Player) -> None:
        """抽牌"""
        player.add_cards_to_hand([self._cards.pop()])


class Card:
    """類別：卡牌"""

    def __init__(self, rank: str, suit: str) -> None:
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """取得卡牌的 _rank 屬性內容（點數）"""
        return self._rank

    @property
    def suit(self):
        """取得卡牌的 _suit 屬性內容（花色）"""
        return self._suit

    def __repr__(self) -> str:
        return f"Card(Rank={self._rank}, Suit={self._suit})"

    def __gt__(self, card: "Card"):
        """設定大小判斷依據"""
        if SUIT_LOOKUP[self._suit] > SUIT_LOOKUP[card.suit]:
            return True
        elif SUIT_LOOKUP[self._suit] < SUIT_LOOKUP[card.suit]:
            return False
        else:
            if RANK_LOOKUP[self.rank] > RANK_LOOKUP[card._rank]:
                return True
            else:
                return False


class Hand:
    """手牌類別"""

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._all_cards = []

    @property
    def all_cards(self):
        """取得 _all_cards 屬性內容"""
        return self._all_cards

    @all_cards.setter
    def all_cards(self, cards: List[Card]):
        self._all_cards = cards

    def add_cards(self, cards: List[Card]):
        """新增一些牌到手牌中"""
        self._all_cards += cards

    def get_hand_size(self) -> int:
        """計算手牌張數"""
        return len(self._all_cards)

    def show_card(self, card_index: int) -> Card:
        """出牌"""
        removed_card = self._all_cards[card_index]
        print(f"{removed_card} showed.")
        self._all_cards.remove(removed_card)
        return removed_card

    def show_random_card(self):
        """隨機出牌"""
        card_index = random.randint(0, len(self._all_cards) - 1)
        return self.show_card(card_index)


class HandExchange:
    """關聯類別：手牌交換"""

    def __init__(self, keep_rounds: int) -> None:
        self.exchange_records = {}
        self.keep_rounds = keep_rounds

    def exchange(
        self, source_player: Player, target_player: Player, start_round: int
    ) -> None:
        """執行手牌交換"""
        print(
            f"Hand Exchang happened at round {start_round}, from {source_player} "
            f"to {target_player}."
        )
        source_player.hand, target_player.hand = (
            target_player.hand,
            source_player.hand,
        )
        source_player.is_exchanged_hand = True
        self.exchange_records.update(
            {
                source_player.name: {
                    "target_player": target_player,
                    "start_round": start_round,
                    "rest_rounds": self.keep_rounds,
                }
            }
        )

    def countdown(self) -> None:
        """計算交換剩餘的回合數"""
        for record in self.exchange_records.values():
            if record["rest_rounds"] > 0:
                record["rest_rounds"] -= 1
