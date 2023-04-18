from card import Deck, RANK_LOOKUP, SUIT_LOOKUP, HandExchange
from player import Player


class Showdown:
    def __init__(self, players: list, round_num: int = 13):
        self._deck = Deck()
        if len(players) == 4:
            self._players = {i: k for i, k in enumerate(players)}
        else:
            raise Exception("The game can only have 4 players, please check.")
        self._round_num = round_num
        self._current_round = 1
        self._current_round_cards_show = {}
        self._exchanger = HandExchange(keep_rounds=3)
        self._winner_each_round = {}

    def prerequisite(self) -> None:
        print("Shuffling Deck...\n")
        self._deck.shuffle()

        print("Now, draw cards until every players have 13 cards in hand.\n")
        while self._players[3]._hand.get_hand_size() < 13:
            for player in self._players.values():
                self._deck.drawcard(player=player)

        assert len(self._deck._cards) == 0
        print("Show all cards:\n")
        for i, player in self._players.items():
            print(f"Player#{i} - {player.name} has hand cards: {player._hand._all_cards}")

    def exchange_process(self) -> None:
        for player in self._players.values():
            if not player._is_exchanged_hand:
                is_exchange, exg_target = player.decide_exchange(round_num=self._round_num, players=[p for p in self._players.values() if p.name != player.name])
                if is_exchange:
                    self._exchanger.exchange(source_player=player, target_player=exg_target, start_round=self._current_round)
        
        self._exchanger.countdown()

    def showcard_process(self) -> None:
        print(f" Show cards: \n")
        for i, player in self._players.items():
            card = player.showcard()
            print(f"Player#{i} - {player.name}: {card}\n")
            self._current_round_cards_show.update({i: card})

    def card_comparison(self) -> Player:
        """返回出牌中花色、數字綜合最大的玩家"""
        cards = {i: {"suit": SUIT_LOOKUP[card._suit], "rank": RANK_LOOKUP[card._rank]} for i, card in self._current_round_cards_show.items()}
        sorted_cards = {k: v for k, v in sorted(cards.items(), key=lambda item: (item[1]["suit"], item[1]["rank"]), reverse=True)}
        winner = self._players[list(sorted_cards.keys())[0]]
        winner.gain_points(points=1)
        print(f"The winner goes to {winner}!\n")
        return winner
    
    def final_result(self) -> Player:
        """返回所有局數結束後，分數最高的玩家"""
        sorted_players = {i: player for i, player in sorted(self._players.items(), key=lambda k: k[1]._point, reverse=True)}
        winner = list(sorted_players.values())[0]

        print("***** Game Results *****\n")
        print(f" Final Winner: {winner}\n Winner gain points: {winner._point}\n")
        print(f" Winner of each round: {self._winner_each_round}\n")
        print(f" Points of each players:\n")
        
        for player in self._players.values():
            print(f"Player: {player.name} | points: {player._point}\n")
        print("***   Thank you for playing!   ***\n")
        return winner

    def start(self):
        print("****** New Game Creating ******\n")
        print("Players joining...")
        print(f"There are {len(self._players)} players in this game.\n")
        print(f"We're going to have {self._round_num} rounds. Good luck.\n")

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

        final_winner = self.final_result()
