"""定義抽象類別：賽局、對賽局流程以模板模式抽象"""
import logging
from abc import ABC, abstractmethod
from typing import List, Union

from .card import Deck, Hand


class CardGame(ABC):
    """抽象類別：賽局"""

    def __init__(
        self,
        game_name: str,
        cards: List,
        players: List,
        round_num: int,
        draw_card_num: Union[int, None],
        **kwargs,
    ) -> None:

        self._game_name = game_name
        self._deck = Deck(cards=cards)
        self._players = {i: k for i, k in enumerate(players)}
        self._round_num = round_num
        self._current_round = 1
        self._draw_card_num = draw_card_num
        logging.info(
            "****** New Game Creating ******\n"
            "Players joining..."
            f"There are {len(self._players)} players in this game.\n"
        )

    @abstractmethod
    def prerequisite(self) -> None:
        """遊戲前準備"""

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
            player.hand = Hand()
            player.hand.add_cards(
                [self._deck.draw_card() for i in range(draw_card_num)]
            )
            logging.info(f"Drawed Cards: {player.hand.cards}")

    @abstractmethod
    def round_process(self) -> None:
        pass

    @abstractmethod
    def game_process(self) -> None:
        pass

    @abstractmethod
    def final_result(self) -> None:
        pass

    def start(self):
        """流程執行"""

        self.prerequisite()
        self.game_process()
        self.final_result()
