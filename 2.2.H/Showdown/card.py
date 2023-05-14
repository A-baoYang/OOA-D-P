"""卡牌類的類別"""
import sys

from player import ShowdownPlayer

sys.path.append("..")
from CardGame.card import Card, Hand, Deck

RANK = [str(i) for i in list(range(2, 11))] + ["J", "Q", "K", "A"]
RANK_LOOKUP = {k: i for i, k in enumerate(RANK)}
SUIT = ["CLUB", "DIAMOND", "HEART", "SPADE"]
SUIT_LOOKUP = {k: i for i, k in enumerate(SUIT)}


class ShowdownCard(Card):
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

    def __gt__(self, card: "ShowdownCard"):
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


class HandExchange:
    """關聯類別：手牌交換"""

    def __init__(self, keep_rounds: int) -> None:
        self.exchange_records = {}
        self.keep_rounds = keep_rounds

    def exchange(
        self,
        source_player: ShowdownPlayer,
        target_player: ShowdownPlayer,
        start_round: int,
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
