import random
import consts

def create():
    game_field = []
    for i in range (consts.NUM_OF_ROWS):
        game_field.append([])
        for j in range (consts.NUM_OF_COLS):
            game_field[i].append("_")
    random_mines(game_field)
    flag_in_field(game_field)
    return game_field

def random_mines(game_field):
    for i in range(consts.NUM_OF_MINES):
        rndm_num_1 = random.randint(1, consts.NUM_OF_ROWS-1)
        rndm_num_2 = random.randint(1, consts.NUM_OF_COLS-1)
        while 21 <= rndm_num_1 <=23 and 46 <= rndm_num_2 <=49:
            continue
        else:
            game_field[rndm_num_1][rndm_num_2] = "X"

def flag_in_field(game_field):
    for i in range(consts.NUM_OF_MINES):
        for j in range(consts.NUM_OF_COLS):
            if 21 <= i <=23 and 46 <= j <= 49:
                game_field[i][j] = "F"
            else:
                pass

def get_legs_location():
