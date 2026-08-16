import random
RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

NUM_OF_ROWS = 25
NUM_OF_COLS = 50
NUM_OF_MINES = 20

KEYS = ["up", "down", "left", "right"]

BACKGROUND_COLOR = (00 ,33 ,00)
DISPLAY_SIZE = (500, 250)
GRASS_SIZE = (30, 10)

GRASS_LIST = []
for time in range(22):
    GRASS_PLACMENT_X = random.randrange(0, 470)
    GRASS_PLACMENT_Y = random.randrange(0, 240)
    GRASS_PLACMENT = (GRASS_PLACMENT_X, GRASS_PLACMENT_Y)
    GRASS_LIST.append(GRASS_PLACMENT)