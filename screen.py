from idlelib import window
from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import consts
import random
import game_field


pygame.init()

def display(window):
     #here?
    draw_grass(window)
    draw_flag(window)
    draw_soldier(window)

    return window


def draw_grass(window):
    grass = pygame.image.load('grass.png')
    grass = pygame.transform.scale(grass, consts.GRASS_SIZE)
    for i in consts.GRASS_LIST:
        window.blit(grass, i)
        pygame.display.update()
    return grass

'''window = True
while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False'''

def draw_grid(dark_window):
    for x in range(consts.TILE_SIZE, SCREENWIDTH, consts.TILE_SIZE):
        pygame.draw.line(dark_window, consts.BACKGROUND_COLOR, (x, 0), (x, 250))

    for y in range(consts.TILE_SIZE, SCREENHEIGHT, consts.TILE_SIZE):
        pygame.draw.line(dark_window, consts.BACKGROUND_COLOR, (0, y), (500, y))

    pygame.display.update()
    return

def draw_mines(dark_window):
    mine = pygame.image.load('mine.png')
    mine = pygame.transform.scale(mine, consts.GRASS_SIZE)
    for index in consts.mines:
        dark_window.blit(mine, index)
        pygame.display.update()
    return

def draw_flag(window):
    flag = pygame.image.load('flag.png')
    flag = pygame.transform.scale(flag, consts.FLAG_SIZE)
    window.blit(flag, consts.FLAG_PLACMENT)
    pygame.display.update()
    return

def draw_soldier(window):
    soldier = pygame.image.load('soldier.png')
    soldier = pygame.transform.scale(soldier, consts.SOLDIER_SIZE)
    window.blit(soldier, (consts.SOLDIER_PLACMENT_X, consts.SOLDIER_PLACMENT_Y))
    pygame.display.update()
    return

'''def draw_explosion(window):
    explosion = pygame.image.load('explotion.png')
    explosion = pygame.transform.scale(explosion, consts.GRASS_SIZE)
    window.blit(explosion, consts.explo_PLACMENT)
    return'''


def draw_night_soldier(dark_window):
    night_soldier = pygame.image.load('soldier_nigth.png')
    night_soldier = pygame.transform.scale(night_soldier, consts.SOLDIER_SIZE)
    dark_window.blit(night_soldier, consts.SOLDIER_PLACMENT)
    pygame.display.update()
    return

def dark_mode(window):
    window.fill(consts.BC_DARK)
    pygame.display.flip() #here?
    draw_grid(window, )
    draw_mines(window)
    draw_night_soldier(window)
    return window


def draw_lose_message(window):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    lose_img = font.render(consts.LOSE_MESSAGE, True, consts.COLOR)
    window.blit(lose_img, consts.LOSE_LOCATION)

def draw_win_message(window):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    win_img = font.render(consts.WIN_MESSAGE, True, consts.COLOR)
    window.blit(win_img, consts.LOSE_LOCATION)




