class Hand:
    def __init__(self) -> None:
        self.card_list = []
        pass

    def append(self, card) -> None:
        self.card_list.append(card)
    
    def size(self) -> int:
        return len(self.card_list)
    
