"""賽局流程"""
from card import Deck, HandExchange
from player import Player


class Showdown:
    """類別：賽局"""

    def __init__(self, players: list, round_num: int = 13):
        self.deck = Deck()

        if len(players) == 4:
            self.players = {i: k for i, k in enumerate(players)}
        else:
            raise TypeError("The game can only have 4 players, please check.")
        self._round_num = round_num
        self._current_round = 1
        self._current_round_cards_show = {}
        self._exchanger = HandExchange(keep_rounds=3)
        self._winner_each_round = {}

    def prerequisite(self) -> None:
        """遊戲前準備"""
        print("Shuffling Deck...\n")
        self.deck.shuffle()

        print("Now, draw cards until every players have 13 cards in hand.\n")
        while self.players[3].hand.get_hand_size() < 13:
            for player in self.players.values():
                self.deck.drawcard(player=player)

        assert len(self.deck.cards) == 0
        print("Show all cards:\n")
        for i, player in self.players.items():
            print(f"Player#{i} - {player.name} has hand cards: {player.hand.all_cards}")

    def exchange_process(self) -> None:
        """遊戲程序：手牌交換"""
        for player in self.players.values():
            if not player.is_exchanged_hand:
                [is_exchange, exg_target] = player.decide_exchange(
                    round_num=self._round_num,
                    players=[p for p in self.players.values() if p.name != player.name],
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
        for i, player in self.players.items():
            card = player.showcard()
            print(f"Player#{i} - {player.name}: {card}\n")
            self._current_round_cards_show.update({i: card})

    def card_comparison(self) -> Player:
        """遊戲程序：返回該回合勝利的玩家（出牌花色點數最大）"""
        sorted_cards = dict(
            sorted(
                self._current_round_cards_show.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )
        winner = self.players[list(sorted_cards.keys())[0]]
        winner.gain_points(points=1)
        print(f"The winner goes to {winner}!\n")
        return winner

    def final_result(self) -> None:
        """遊戲程序：返回所有局數結束後，分數最高的玩家"""
        winners, max_point = [], 0
        for p in self.players.values():
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

        for player in self.players.values():
            print(f"Player: {player.name} | points: {player.point}\n")
        print("***   Thank you for playing!   ***\n")

    def start(self):
        """流程執行"""
        print(
            "****** New Game Creating ******\n"
            "Players joining..."
            f"There are {len(self.players)} players in this game.\n"
            f"We're going to have {self._round_num} rounds. Good luck.\n"
        )

        self.prerequisite()

        print("***    Game Start!    ***\n\n")
        while self._current_round <= 13:
            print(f"----- Round {self._current_round} -----\n\n")
            self.exchange_process()
            self.showcard_process()
            winner = self.card_comparison()
            self._winner_each_round.update({self._current_round: winner.name})
            self._current_round += 1
            self._current_round_cards_show = {}

        self.final_result()
