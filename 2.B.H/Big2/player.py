"""定義玩家相關屬性與方法"""
import random
from typing import Union
import logging
from CardGame import Player
from CardGame.utils import check_input_valid


class Big2Player(Player):
    """繼承類別：大老二玩家"""

    def __init__(self) -> None:
        super().__init__()
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, player: "Big2Player"):
        self._next = player


class HumanPlayer(Big2Player):
    """繼承類別：真人玩家"""

    def __init__(self) -> None:
        super().__init__()

    def name_himself(self) -> None:
        name = input("Please name yourself: ")
        assert isinstance(name, str), TypeError("name 需為字串")
        self._name = name
        print(self)

    def show_card(self) -> list:
        """選擇卡牌，以牌型類別打出"""
        sorted_cards = {i: c for i, c in enumerate(sorted(self._hand.cards))}
        formatted_sorted_cards = "".join(
            [f"{str(c) : <7}" for c in sorted_cards.values()]
        )
        formatted_numbers = "".join([f"{i : <7}" for i in sorted_cards.keys()])
        card_indices = ""
        while not check_input_valid(card_indices):
            card_indices = input(
                f"輪到 Player {self._name} 了\n{formatted_numbers}\n{formatted_sorted_cards}\n"
                "請選擇出牌牌型 (以半形逗號分開)\n若無符合資格牌型請輸入 -1 以 PASS 這一回合: \n"
            )
        if card_indices == "-1":
            cards_to_show = []
        else:
            card_indices = [int(i) for i in card_indices.split(",")]
            cards_to_show = self.hand.get_cards(card_indices=card_indices)
        logging.info(cards_to_show)
        return cards_to_show

    def show_pattern(
        self,
        assign_pattern: Union["CardPattern", None] = None,
        benchmark: Union["CardPattern", None] = None,
        is_first_round: bool = False,
    ) -> Union["CardPattern", None]:
        """選擇卡牌，以牌型類別打出"""
        card_pattern = self._show_pattern()
        # 第一局開局時
        if is_first_round and not assign_pattern:
            while card_pattern == "PASS" or not self.hand.is_contains_club_3(
                cards=card_pattern.cards
            ):
                logging.warn("第一局開局出牌需包含梅花 3，不可跳過，請重新出牌")
                card_pattern = self._show_pattern()
        # 每回合的第一人出牌時
        elif not is_first_round and not assign_pattern:
            while card_pattern == "PASS":
                logging.warn("每回合開局出牌無限制，只要符合 4 種格式其中一種，不可跳過，請重新出牌")
                card_pattern = self._show_pattern()
                logging.info(card_pattern)
        # 其他所有情境
        elif benchmark and assign_pattern:
            if card_pattern == "PASS":
                return card_pattern
            while not isinstance(card_pattern, assign_pattern) or benchmark.compare(
                card_pattern=card_pattern
            ):
                logging.warn("出牌需符合目前頂牌格式且大於目前頂牌，請重新出牌")
                card_pattern = self._show_pattern()
                if card_pattern == "PASS":
                    return card_pattern
        else:
            raise Exception("出牌環節遇到未設定過的情境，請檢查程式")

        self.hand.remove_cards(cards_to_remove=card_pattern.cards)
        logging.info(f"{card_pattern} Showed")
        return card_pattern

    def _show_pattern(self) -> Union["CardPattern", str]:
        is_type_passed = False
        while not is_type_passed:
            cards = self.show_card()
            if cards:
                try:
                    card_pattern = self.hand._card_pattern_handler.single(cards=cards)
                    logging.info(card_pattern)
                    is_type_passed = True
                except TypeError as e:
                    logging.error(e)
            else:
                return "PASS"
        return card_pattern


class AIPlayer(Big2Player):
    """繼承：電腦虛擬玩家"""

    def __init__(self) -> None:
        super().__init__()

    def name_himself(self) -> None:
        self._name = f"AI #{random.randint(1, 10 ** 5)}"
        print(self)

    def show_card(self, card_choices: list) -> list:
        if card_choices:
            card_indices = self.hand.show_random_card(card_choices=card_choices)
            cards_to_show = self.hand.get_cards(card_indices=card_indices)
            logging.info(cards_to_show)
        else:
            cards_to_show = []
        return cards_to_show

    def show_pattern(
        self,
        assign_pattern: Union["CardPattern", None] = None,
        benchmark: Union["CardPattern", None] = None,
        is_first_round: bool = False,
    ) -> list:
        print(f"輪到 Player {self._name} 了\n")
        card_pattern = self._show_pattern(benchmark=benchmark, is_first_round=is_first_round)
        # 第一局開局時
        if is_first_round and not assign_pattern:
            while card_pattern == "PASS" or not self.hand.is_contains_club_3(
                cards=card_pattern.cards
            ):
                logging.warn("第一局開局出牌需包含梅花 3，不可跳過，請重新出牌")
                card_pattern = self._show_pattern(benchmark=benchmark, is_first_round=is_first_round)
        # 每回合的第一人出牌時
        elif not is_first_round and not assign_pattern:
            while card_pattern == "PASS":
                logging.warn("每回合開局出牌無限制，只要符合 4 種格式其中一種，不可跳過，請重新出牌")
                card_pattern = self._show_pattern(benchmark=benchmark, is_first_round=is_first_round)
                logging.info(card_pattern)
        # 其他所有情境
        elif benchmark and assign_pattern:
            if card_pattern == "PASS":
                return card_pattern
            while not isinstance(card_pattern, assign_pattern) or benchmark.compare(
                card_pattern=card_pattern
            ):
                logging.warn("出牌需符合目前頂牌格式且大於目前頂牌，請重新出牌")
                card_pattern = self._show_pattern(benchmark=benchmark, is_first_round=is_first_round)
                if card_pattern == "PASS":
                    return card_pattern
        else:
            raise Exception("出牌環節遇到未設定過的情境，請檢查程式")

        self.hand.remove_cards(cards_to_remove=card_pattern.cards)
        logging.info(f"{card_pattern} Showed")
        return card_pattern

    def _show_pattern(
        self,
        benchmark: Union["CardPattern", None] = None,
        is_first_round: bool = False,
    ) -> Union["CardPattern", str]:

        card_choices = self.hand.show_random_pattern(
            hand=self.hand, top_play=benchmark, is_first_round=is_first_round
        )
        is_type_passed = False
        while not is_type_passed:
            cards = self.show_card(card_choices=card_choices)
            if cards:
                try:
                    card_pattern = self.hand._card_pattern_handler.single(cards=cards)
                    logging.info(card_pattern)
                    is_type_passed = True
                except TypeError as e:
                    logging.error(e)
            else:
                return "PASS"
        return card_pattern


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
