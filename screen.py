import pygame

pygame.init()

window = pygame.display.set_mode((500, 250))
pygame.display.set_caption('flag')

window.fill(green)
pygame.display.flip()
mine = pygame.image.load('mine.png')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit() #?