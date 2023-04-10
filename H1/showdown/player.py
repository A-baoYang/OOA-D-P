from abc import ABC

from card import Hand, Card


class Player(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self._hand = Hand(owner=self.name)
        self._point = 0

    def change_name(self, newname) -> None:
        self.name = newname
        self._hand.owner = self.name
    
    def add_cards_to_hand(self, cards) -> None:
        for card in cards:
           self._hand._all_cards.append(card)

    def showcard(self, card: Card) -> Card:
        self._hand._all_cards.remove(card)
        return card

    def gain_points(self, points: int) -> None:
        self._point += 1

    def __repr__(self) -> str:
        return f"Player: {self.name}"


class HumanPlayer(Player):
    def __init__(self, name = "Anonymous") -> None:
        super().__init__(name)

    # def showcard(self) -> Card:
    #     return self._hand.show_random_card()
    

class AIPlayer(Player):
    def __init__(self, name = "Anonymous") -> None:
        super().__init__(name)

    def showcard(self) -> Card:
        return self._hand.show_random_card()
