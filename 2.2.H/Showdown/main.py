"""程式啟動點"""
from itertools import product
from showdown import Showdown
from card import ShowdownCard, RANK, SUIT
from player import AIPlayer, HumanPlayer


if __name__ == "__main__":
    players = [HumanPlayer() for i in range(4)]
    showdown = Showdown(
        game_name="Showdown 比大小",
        cards=[
            ShowdownCard(rank=item[0], suit=item[1]) for item in product(RANK, SUIT)
        ],
        players=players,
        round_num=13,
    )
    showdown.start()
