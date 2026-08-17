import random
import consts

def create():
    game_field = []
    for i in range (consts.NUM_OF_ROWS):
        game_field.append([])
        for j in range (consts.NUM_OF_COLS):
            game_field[i].append(consts.EMPTY)
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
            game_field[rndm_num_1][rndm_num_2] = consts.MINE
            consts.mines.append((rndm_num_2*10, rndm_num_1*10))

def flag_in_field(game_field):
    for i in range(consts.NUM_OF_MINES):
        for j in range(consts.NUM_OF_COLS):
            if 21 <= i <=23 and 46 <= j <= 49:
                game_field[i][j] = consts.FLAG
            else:
                pass

def calc_body(game_field):
    count = 0
    body = []
    while count <= 6:
        for i in range(consts.NUM_OF_MINES):
            for j in range(consts.NUM_OF_COLS):
                if game_field[i][j] == consts.SOLDIER:
                    body.append([i, j])
                    count += 1
    return body

def calc_legs():
    count = 0
    legs = []
    for i in range(consts.NUM_OF_MINES):
        for j in range(consts.NUM_OF_COLS):
            count += 1
            if game_field[i][j] == consts.SOLDIER and 6<=count<=8:
                legs.append([i, j])
    return legs

def calc_whole_soldier(game_field):
    whole_soldier = []
    for i in range(consts.NUM_OF_MINES):
        for j in range(consts.NUM_OF_COLS):
            if game_field[i][j] == consts.SOLDIER:
                whole_soldier.append([i, j])
    return whole_soldier
#def get_legs_location():