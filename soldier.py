import pygame
import consts
import game_field
import screen

def create_soldier():
    soldier = pygame.image.load('soldier.png')
    soldier = pygame.transform.scale(soldier, consts.SOLDIER_SIZE)
    screen.display().blit(soldier, consts.SOLDIER_PLACMENT)
    return soldier

'''def place_soldier():

def calc_body():

def calc_legs():'''

#def move_in_direction(soldier, direction):