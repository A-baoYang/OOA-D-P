from itertools import product

from card import RANK, SUIT, Big2Card
from player import AIPlayer, HumanPlayer
from big2 import Big2
from CardGame.utils import log_setting


if __name__ == "__main__":
    log_setting()

    # players = [HumanPlayer() for i in range(4)]
    players = [HumanPlayer() for i in range(2)] + [AIPlayer() for i in range(2)]
    big2_game = Big2(
        game_name="Big2",
        cards=[Big2Card(rank=item[0], suit=item[1]) for item in product(RANK, SUIT)],
        players=players,
    )
    big2_game.start()
