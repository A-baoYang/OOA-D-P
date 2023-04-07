from card import Hand
from abc import ABC


class Player(ABC):
    def __init__(self) -> None:
        self.name = ""
        self.hand = Hand()

    def naming(self, name) -> None:
        self.name = name
    
    def addCardToHand(self, card) -> None:
        self.hand.append(card)


class HumanPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
    

