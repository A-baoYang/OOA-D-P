from abc import ABC
import random


class Player(ABC):
    def __init__(self, name) -> None:
        from card import Hand

        self.name = name
        self._hand = Hand(owner=self.name)
        self._point = 0
        self._is_exchanged_hand = False

    def change_name(self, newname) -> None:
        self.name = newname
        self._hand.owner = self.name
    
    def add_cards_to_hand(self, cards) -> None:
        for card in cards:
           self._hand._all_cards.append(card)

    def showcard(self, card):
        self._hand._all_cards.remove(card)
        return card

    def gain_points(self, points: int) -> None:
        self._point += points

    def decide_exchange(self):
        pass

    def __repr__(self) -> str:
        return f"Player: {self.name}"


class HumanPlayer(Player):
    def __init__(self, name = "Anonymous") -> None:
        super().__init__(name)

    def showcard(self, card):
        return super().showcard(card)


class AIPlayer(Player):
    def __init__(self, name = "Anonymous") -> None:
        super().__init__(name)

    def showcard(self):
        return self._hand.show_random_card()

    def decide_exchange(self, round_num, players) -> tuple:
        is_exchange = random.choices([0, 1], [0.5+1/round_num,  0.5-1/round_num])[0]
        exchange_player = random.choice(players)
        return is_exchange, exchange_player
