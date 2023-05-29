from itertools import product

from card import RANK, SUIT, Big2Card
from player import AIPlayer, HumanPlayer
import logging
from big2 import Big2
from utils import log_setting


if __name__ == "__main__":
    log_setting()

    players = [HumanPlayer() for i in range(4)]
    big2_game = Big2(
        game_name="UNO 101",
        cards=[Big2Card(rank=item[0], suit=item[1]) for item in product(RANK, SUIT)],
        players=players,
    )
    big2_game.start()
