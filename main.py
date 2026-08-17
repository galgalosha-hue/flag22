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
            state["is_window_open"] = False
        elif is_win():
            state["state"] = consts.WIN_STATE
            time.sleep(3)
            state["is_window_open"] = False

        screen.draw_game(state)

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
                handle_user_button(key)

def handle_user_button(key):
    whole_soldier = calc_whole_soldier(game_field)
    if key == pygame.K_LEFT and consts.SOLDIER_PLACMENT_X > 0:
        soldier.move_left(whole_soldier)
    elif key == pygame.K_RIGHT and consts.SOLDIER_PLACMENT_X+20 < 500:
            soldier.move_right(whole_soldier)
    elif key == pygame.K_UP and consts.SOLDIER_PLACMENT_Y > 0:
            soldier.move_up(whole_soldier)
    elif key == pygame.K_DOWN and consts.SOLDIER_PLACMENT_Y+40 < 250:
            soldier.move_down(whole_soldier)
    else:
        pass

def handle_user_enter():
    #show other screen for 1 second

def is_touching_flag():
    #if body in indexes at the same row as flags but the column is -1
    #if body indexes (x,y) == flag placement
    body = soldier.calc_body(game_field)
    '''for i in body:
        for j in range (len(body[i])):
            if body[i][j] =='''
    for i in range(len(body)):
        if i%2 != 0:
            for j in range(len(body[i])):
                if j == 0:
                    if

def is_touching_mine(game_field):
    #if leg column is -1 or +1 of the minse OR the column is the same and the row is -1
    #if leg indexes (x,y) == mine placement
    soldier.calc_legs(game_field)
    for i in range(len(game_field)):
        for j in game_field[i]:


def is_lose():
    if is_touching_mine(game_field):
        return True
    else:
        return False
        
def is_win():
    if is_touching_flag(game_field):
        return True
    else:
        return False

main()