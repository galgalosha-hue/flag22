from idlelib import window
from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import consts
import random

import game_field

pygame.init()

def display():
    window = pygame.display.set_mode(consts.DISPLAY_SIZE)
    pygame.display.set_caption('flag')
    window.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
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

def draw_grid(TILE_SIZE, window):
    for x in range(TILE_SIZE, SCREENWIDTH, TILE_SIZE):
        pygame.draw.line(window, consts.BACKGROUND_COLOR, (x, 0), (x, 250))

    for y in range(TILE_SIZE, SCREENHEIGHT, TILE_SIZE):
        pygame.draw.line(window, consts.BACKGROUND_COLOR, (0, y), (500, y))

    pygame.display.update()
    return

def draw_mines(window):
    mine = pygame.image.load('mine.png')
    mine = pygame.transform.scale(mine, consts.GRASS_SIZE)
    for index in consts.mines:
        window.blit(mine, index)
        pygame.display.update()
    return

def draw_flag(window):
    flag = pygame.image.load('flag.png')
    flag = pygame.transform.scale(flag, consts.FLAG_SIZE)
    window.blit(flag, consts.FLAG_PLACMENT)
    return

def draw_soldier(window):
    soldier = pygame.image.load('soldier.png')
    soldier = pygame.transform.scale(soldier, consts.SOLDIER_SIZE)
    window.blit(soldier, consts.SOLDIER_PLACMENT)
    return

'''def draw_explosion(window):
    explosion = pygame.image.load('explotion.png')
    explosion = pygame.transform.scale(explosion, consts.GRASS_SIZE)
    window.blit(explosion, consts.explo_PLACMENT)
    return'''



def draw_night_soldier(window):
    night_soldier = pygame.image.load('soldier_nigth.png')
    night_soldier = pygame.transform.scale(night_soldier, consts.SOLDIER_SIZE)
    window.blit(night_soldier, consts.SOLDIER_PLACMENT)
    return



