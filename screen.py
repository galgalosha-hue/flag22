import pygame
import consts
pygame.init()

def display():
    window = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption('flag')
    window.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
    return window

def draw_grass(window):
    for bush in range(20):
        grass = pygame.image.load('grass.png')
        grass = pygame.transform.scale(grass, GRASS_SIZE)
        window.blit(grass, GRASS_PLACMENT)
    pygame.display.flip()
    return grass

