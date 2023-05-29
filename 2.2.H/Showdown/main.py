"""程式啟動點"""
from itertools import product

from .card import RANK, SUIT, ShowdownCard
from .player import AIPlayer, HumanPlayer
from .showdown import Showdown

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
