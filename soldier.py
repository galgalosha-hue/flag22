import pygame
import consts
import game_field
import screen

def create_soldier():
    soldier = pygame.image.load('soldier.png')
    soldier = pygame.transform.scale(soldier, consts.SOLDIER_SIZE)
    screen.display().blit(soldier, consts.SOLDIER_PLACMENT)
    return soldier

def place_soldier(game_field):
    for i in range(consts.NUM_OF_MINES):
        for j in range(consts.NUM_OF_COLS):
            if 0 <= i <= 2 and 0 <= j <= 1:
                game_field[i][j] = consts.SOLDIER
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

def move_right(whole_soldier):
    for i in range(len(whole_soldier)):
        for j in range(2):
            whole_soldier[i][j] = whole_soldier[i][j] + 1
    consts.SOLDIER_PLACMENT_X += consts.STEP

def move_left(whole_soldier):
    for i in range(len(whole_soldier)):
        for j in range(2):
            whole_soldier[i][j] = whole_soldier[i][j] - 1
    consts.SOLDIER_PLACMENT_X -= consts.STEP

def move_up(whole_soldier):
    for i in range(len(whole_soldier)):
        for j in range(1):
            whole_soldier[i][j] = whole_soldier[i][j] - 1
    consts.SOLDIER_PLACMENT_Y -= consts.STEP

def move_down(whole_soldier):
    for i in range(len(whole_soldier)):
        for j in range(1):
            whole_soldier[i][j] = whole_soldier[i][j] + 1
    consts.SOLDIER_PLACMENT_Y += consts.STEP