import random
import consts

def create():
    game_field = []
    for i in range (consts.NUM_OF_ROWS):
        game_field.append([])
        for j in range (consts.NUM_OF_COLS):
            game_field[i].append("_")
    return game_field

def random_mines(game_field):
    for i in range(consts.NUM_OF_MINES):
        rndm_num_1 = random.randint(1, consts.NUM_OF_ROWS)
        rndm_num_2 = random.randint(1, consts.NUM_OF_COLS)
        game_field[rndm_num_1][rndm_num_2] = "X"

