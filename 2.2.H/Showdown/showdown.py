"""賽局流程實例化"""
import sys
from card import HandExchange
from player import ShowdownPlayer
from typing import Union

sys.path.append("..")
from CardGame.cardgame import CardGame


class Showdown(CardGame):
    """類別：賽局"""

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

        self._current_round_cards_show = {}
        self._exchanger = HandExchange(keep_rounds=3)
        self._winner_each_round = {}

    def exchange_process(self) -> None:
        """遊戲程序：手牌交換"""
        for player in self._players.values():
            if not player.is_exchanged_hand:
                [is_exchange, exg_target] = player.decide_exchange(
                    round_num=self._round_num,
                    players=[
                        p for p in self._players.values() if p.name != player.name
                    ],
                )
                if is_exchange:
                    self._exchanger.exchange(
                        source_player=player,
                        target_player=exg_target,
                        start_round=self._current_round,
                    )

        self._exchanger.countdown()

    def showcard_process(self) -> None:
        """遊戲程序：出牌階段"""
        print(" Show cards: \n")
        for i, player in self._players.items():
            card = player.show_card()
            print(f"Player#{i} - {player.name}: {card}\n")
            self._current_round_cards_show.update({i: card})

    def card_comparison(self) -> ShowdownPlayer:
        """遊戲程序：返回該回合勝利的玩家（出牌花色點數最大）"""
        sorted_cards = dict(
            sorted(
                self._current_round_cards_show.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
        winner = self._players[list(sorted_cards.keys())[0]]
        winner.gain_points(points=1)
        print(f"The winner goes to {winner}!\n")
        return winner

    def prerequisite(self) -> None:
        return super().prerequisite()

    def round_process(self) -> None:
        """實例化單局程序"""
        self.exchange_process()
        self.showcard_process()
        winner = self.card_comparison()
        self._winner_each_round.update({self._current_round: winner.name})
        self._current_round_cards_show = {}

    def game_process(self) -> None:
        """實例化遊戲程序"""
        self._logger.info("***    Game Start!    ***\n\n")
        if self._round_num > 0:
            self._logger.info(
                f"We're going to have {self._round_num} rounds. Good luck.\n"
            )
            while self._current_round <= self._round_num:
                self._logger.info(f"----- Round {self._current_round} -----\n\n")
                self.round_process()
                self._current_round += 1
        else:
            self._logger.error(
                "round_num must > 0 to use default game_process, or you need to provide your winning condition"
            )

    def final_result(self) -> None:
        """實例化結算程序：返回所有局數結束後，分數最高的玩家"""
        winners, max_point = [], 0
        for p in self._players.values():
            if p.point > max_point:
                winners = [p]
                max_point = p.point
            elif p.point == max_point:
                winners.append(p)
            else:
                pass

        print(
            "***** Game Results *****\n"
            f" Final Winner: {winners}\n Winner gain points: {max_point}\n"
            f" Winner of each round: {self._winner_each_round}\n"
            " Points of each players:\n"
        )

        for player in self._players.values():
            print(f"Player: {player.name} | points: {player.point}\n")
        print("***   Thank you for playing!   ***\n")

    def start(self):
        return super().start()
