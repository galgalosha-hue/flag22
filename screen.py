from idlelib import window
from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import consts
import random
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
        window.blit(grass, consts.GRASS_PLACMENT)
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

