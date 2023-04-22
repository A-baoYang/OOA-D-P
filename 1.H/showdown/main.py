"""docstring"""
from showdown import Showdown
from player import AIPlayer, HumanPlayer


if __name__ == "__main__":

    p1, p2, p3, p4 = AIPlayer(), AIPlayer(), HumanPlayer(), HumanPlayer()
    showdown = Showdown(players=[p1, p2, p3, p4], round_num=13)
    showdown.start()
