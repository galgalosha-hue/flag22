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
    pygame.display.flip()
    return grass

'''window = True
while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False'''
