import pygame
import consts
import game_field
import screen
import soldier
import time

from soldier import calc_whole_soldier

'''state = {
    "original_arrow": Screen.create_arrow(consts.ARROW_IMG),
    "rotated_arrow": None,
    "is_bubble_fired": False,
    "bubbles_popping": [],
    "turns_left_to_add_row": consts.NUM_OF_TURNS_TO_ADD_ROW,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "bullet_bubble": None,
    "bubble_direction": None,
    "mouse_angle": None
}'''

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,

}

def main():
    pygame.init()
    game_field.create()

    while state["is_window_open"]:

        handle_user_events()

        if is_lose():
            state["state"] = consts.LOSE_STATE
            time.sleep(3)
        elif is_win():
            state["state"] = consts.WIN_STATE
            time.sleep(3)

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] != consts.RUNNING_STATE:
            continue
        if event.type == pygame.KEYDOWN:
            key=pygame.key.name(event.key)
            if key == pygame.K_RETURN:
                handle_user_enter()
            elif key not in consts.KEYS:
                pass
            else:
                game_field.get_legs_location()
                handle_user_button(key)

def handle_user_button(key):
    whole_soldier = calc_whole_soldier(game_field)
    if key == pygame.K_LEFT:
        #if at least one column of his body == 0 THEN DON'T
        #else:
        soldier.move_left(whole_soldier)
    elif key == pygame.K_RIGHT:
        # if at least one column of his body == 24 THEN DON'T
        # else:
        soldier.move_right(whole_soldier)
    elif key == pygame.K_UP:
        # if at least one row of his body == 0 THEN DON'T
        # else:
        soldier.move_up(whole_soldier)
    else:
        # if at least one row of his body == 49 THEN DON'T
        # else:
        soldier.move_down(whole_soldier)



def handle_user_enter():

def is_touching_flag():
    body = soldier.calc_body(game_field)
    for i in body:
        for j in range (len(body[i])):
            if body[i][j] ==

'''def is_touching_mine(game_field):
    soldier.calc_legs(game_field)
    for i in range(len(game_field)):
        for j in game_field[i]:'''



'''def is_lose():

def is_win():'''

