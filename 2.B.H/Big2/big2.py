"""賽局流程實例化"""
import logging
from typing import Union

from card import Big2Card, Big2Hand
from card_pattern import Single, Pair, Straight, FullHouse, CardPatternChain
from CardGame import CardGame, Card
from utils import log_setting


class PlayerChain:
    def __init__(self, players: dict) -> None:
        self._players = players
        for i, p in self._players.items():
            if i == len(self._players) - 1:
                p.next = self._players[0]
            else:
                p.next = self._players[i + 1]

    @property
    def players(self):
        return self._players


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
        self._card_pattern_chain = CardPatternChain()
        self._card_pattern_chain.chain()
        self._top_play = None
        self._top_play_type = None
        self._top_player = None
        self._winner = None
        log_setting()

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
            if [
                card
                for card in player.hand.cards
                if card.rank == "3" and card.suit == "C"
            ]:
                self._top_player = player
            player = player.next

    def showcard_process(self) -> None:
        """遊戲程序：出牌與比較階段"""
        showed_player_count, pass_count, current_player = 0, 0, self._top_player
        while showed_player_count < 4 or pass_count < 3:
            # 出牌
            showed_cards = current_player.show_card()
            if showed_cards is None:
                pass_count += 1
            else:
                showed_pattern = self._card_pattern_chain.single(cards=showed_cards)
                self._each_round_cards_show.update(
                    {current_player.name: showed_pattern.cards}
                )
                if self._top_play is None:
                    self._top_play = showed_pattern
                    logging.info(f"頂牌已更新: {self._top_play.cards}")
                else:
                    # 比大小
                    if self._top_play.compare(card_pattern=showed_pattern):
                        pass
                    else:
                        self._top_play = showed_pattern
                        self._top_play_type = type(self._top_play)
                        self._top_player = current_player
                        logging.info(f"頂牌已更新: {self._top_play.cards}")

            showed_player_count += 1
            current_player = current_player.next

        if pass_count == 3:
            self._winner = self._top_player

    def round_process(self) -> None:
        """實例化單局程序"""
        logging.info("新的回合開始了。")
        self.showcard_process()

    def game_process(self) -> None:
        """實例化遊戲程序"""
        logging.info(
            "***    大老二遊戲開始!    ***\n\n" "核心規則：首位讓其他三位玩家連續 PASS （出不了更大的牌型）的玩家獲勝!\n"
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
