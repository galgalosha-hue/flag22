import pygame
import consts
import game_field
import screen
import soldier
import time

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
    while not contanting with the window:
        if key == pygame.K_LEFT:
            decrease both cols
        elif key == pygame.K_RIGHT:
            increse both cols
        elif key == pygame.K_UP:
            decrese both rows
        else:
            increse both rows
    else:
        pass


def handle_user_enter():

def is_touching_flag():

def is_touching_mine():


def is_lose():

def is_win():

