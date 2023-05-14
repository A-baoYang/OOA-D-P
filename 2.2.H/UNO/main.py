from itertools import product

from uno import UNO
from card import UNOCard, NUMBER, COLOR
from player import AIPlayer, HumanPlayer


if __name__ == "__main__":
    players = [HumanPlayer() for i in range(2)] + [AIPlayer() for i in range(2)]
    showdown = UNO(
        game_name="UNO 101",
        cards=[
            UNOCard(number=item[0], color=item[1]) for item in product(NUMBER, COLOR)
        ],
        players=players,
        draw_card_num=4,
    )
    showdown.start()
