"""賽局流程實例化"""
import sys
from typing import Union

from card import UNOCard
from player import UNOPlayer

sys.path.append("..")
from CardGame import CardGame


class UNO(CardGame):
    """類別：UNO 遊戲"""

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

        self._latest_showed_card = self._deck.draw_card()
        self._winner = None

    def show_card_judge(self, card: UNOCard) -> bool:
        """判斷出牌是否合規"""
        return (
            self._latest_showed_card.color == card.color
            or self._latest_showed_card.number == card.number
        )

    def auto_judge(self, player: UNOPlayer) -> bool:
        """自動判斷玩家是否需要加牌"""
        if not [card for card in player.hand.cards if self.show_card_judge(card=card)]:
            print("No valid card to show, draw a new card...")
            player.hand.add_cards([self._deck.draw_card()])
            return False
        return True

    def prerequisite(self) -> None:
        return super().prerequisite()

    def round_process(self) -> None:
        """實例化單局程序"""
        for i, player in self._players.items():
            if self.auto_judge(player=player):
                while True:
                    print(f"Latest Showed Card: {self._latest_showed_card}")
                    card = player.show_card()
                    card = card[0]
                    # 檢查符合條件
                    if self.show_card_judge(card=card):
                        self._latest_showed_card = card
                        break
                    else:
                        # 防呆機制若出錯牌則加回
                        player.hand.add_cards(cards=[card])
                        self._logger.error(
                            "The card you show isn't align the rule! Please try again"
                        )
            if not player.hand.cards:
                self._winner = player

    def game_process(self) -> None:
        """實例化遊戲程序"""
        print(
            "***    Game Start!    ***\n\n"
            "UNO Game Rule: The very first player whose hand card cleared wins the game!\n"
        )
        while not self._winner:  # 遊戲進行直到決出贏家
            self.round_process()
            self._current_round += 1

    def final_result(self) -> None:
        """實例化結算程序：返回最先清空手牌的玩家"""
        print(
            "***** Game Results *****\n"
            f" Final Winner: {self._winner} (Cleaned hand cards at round#{self._current_round})"
        )

    def start(self):
        return super().start()
