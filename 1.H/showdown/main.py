from showdown import Showdown
from player import AIPlayer


if __name__ == "__main__":
    
    p1, p2, p3, p4 = AIPlayer(name="HHH"), AIPlayer(name="CCC"), AIPlayer(name="OJOJI"), AIPlayer(name="QJWODJPOWJ")
    showdown = Showdown(players=[p1, p2, p3, p4], round_num=13)
    showdown.start()
