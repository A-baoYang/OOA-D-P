"""賽局流程實例化"""
import logging
from typing import Union

from card import Big2Card, Big2Hand
from player import PlayerChain
from card_pattern import CardPatternHandler
from CardGame import CardGame, Card


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
        if len(self._players) == 4:
            pass
        else:
            raise TypeError("The game can only have 4 players, please check.")

        self._player_chain = PlayerChain(players=self._players)
        self._each_round_cards_show = {}
        self._top_play = None
        self._top_player = None
        self._winner = None

    def prerequisite(self) -> None:
        self._deck.shuffle()
        draw_card_num = (
            self._deck.size() // len(self._players)
            if not self._draw_card_num
            else self._draw_card_num
        )
        for i, player in self._players.items():
            # name himself
            logging.info(f"Prerequisite for player#{i}...\n")
            player.name_himself()
            # draw cards to hand
            player.hand = Big2Hand()
            player.hand.add_cards(
                [self._deck.draw_card() for i in range(draw_card_num)]
            )
            logging.info(f"Drawed Cards: {player.hand.cards}")

    def decide_first_player(self) -> None:
        player = self._player_chain._players[0]
        while not self._top_player:
            if player.hand.is_contains_club_3():
                self._top_player = player
                logging.info(f"{self._top_player} 擁有梅花 3，首回合從 {self._top_player} 開始出牌")
            player = player.next

    def showcard_process(self) -> None:
        """遊戲程序：出牌與比較階段"""
        showed_player_count, pass_count, current_player = 0, 0, self._top_player
        self._top_play = None
        is_first_round = self._current_round == 1 and showed_player_count == 0
        while pass_count < 3:
            # 出牌
            showed_pattern = current_player.show_pattern(
                assign_pattern=type(self._top_play) if self._top_play else None,
                benchmark=self._top_play,
                is_first_round=is_first_round,
            )
            if showed_pattern is not None:
                self._top_play = showed_pattern
                self._top_player = current_player
                logging.info(f"頂牌已更新: {self._top_play}")
            else:
                pass_count += 1
                logging.info(f"{current_player} 這一回合 PASS")

            showed_player_count += 1
            if not current_player.hand.cards:
                self._winner = current_player
                break

            current_player = current_player.next

    def round_process(self) -> None:
        """實例化單局程序"""
        logging.info("新的回合開始了。")
        self.showcard_process()

    def game_process(self) -> None:
        """實例化遊戲程序"""
        logging.info(
            "***    大老二遊戲開始!    ***\n\n核心規則：首位讓其他三位玩家連續 PASS（出不了更大的牌型）的玩家獲勝!\n"
        )
        # 決定首位出牌玩家（擁有梅花3的人）
        self.decide_first_player()
        # 遊戲進行直到決出贏家（連三家打不出牌 或 玩家手牌率先打完）
        while not self._winner:
            self.round_process()
            self._current_round += 1

    def final_result(self) -> None:
        """實例化結算程序：返回贏家"""
        logging.info(
            "***** Game Results *****\n"
            f" Final Winner: {self._winner} (Wins at round#{self._current_round})"
        )

    def start(self):
        self.prerequisite()
        self.game_process()
        self.final_result()


# 新的回合由頂牌玩家開始打牌
# 直到有任一玩家將所有的手牌打完為止
