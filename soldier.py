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

def leg_placment():
     s_x = consts.SOLDIER_PLACMENT_X
     s_y = consts.SOLDIER_PLACMENT_Y
     left_leg = (s_x, s_y+40)
     right_leg = (s_x+20, s_y+40)
     return left_leg, right_leg


def soldier_body():
    s_x = consts.SOLDIER_PLACMENT_X
    s_y = consts.SOLDIER_PLACMENT_Y
    head_left = (s_x, s_y)
    head_right = (s_x+20, s_y)
    tummy_left = (s_x, s_y+20)
    tummy_right = (s_x+20, s_y+20)
    return head_left, head_right, tummy_left, tummy_right

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