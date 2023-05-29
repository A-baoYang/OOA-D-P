from card_pattern import Single, Pair, Straight, FullHouse


class CardPatternHandler:
    def __init__(self) -> None:
        self.single = Single()
        self.pair = Pair()
        self.straight = Straight()
        self.fullhouse = FullHouse()

    def chain(self) -> None:
        self.single.next = self.pair
        self.pair.next = self.straight
        self.straight.next = self.fullhouse
