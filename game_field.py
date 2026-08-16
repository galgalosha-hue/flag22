import random
import consts
from consts import NUM_OF_MINES


def create():
    game_field = []
    for i in range (consts.NUM_OF_ROWS):
        game_field.append([])
        for j in range (consts.NUM_OF_COLS):
            game_field[i].append([])

def random_mines:
    rndm_num = random.randint(1, consts.NUM_OF_ROWS)
    for i in range(NUM_OF_MINES):

