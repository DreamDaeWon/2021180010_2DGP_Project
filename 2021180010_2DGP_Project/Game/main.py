from os import closerange

from dw_define import*

from collision import *



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            else:
                key_input_down(event.key)
            pass
        elif event.type == SDL_KEYUP:
            key_input_up(event.key)


    pass


def initialize():
    global world_all
    global collision
    collision = Collision()
    world_all = []
# 추가 순서는 배경->보스->플레이어 순
    #배경 추가


    #보스 추가


    #Player 추가
    world_all.append(CupheadBanging())
    collision.get_player(world_all[0])

    pass

def key_input_down(Key):
    for object in world_all:
        object.key_input_down(Key)

    pass

def key_input_up(Key):
    for object in world_all:
        object.key_input_up(Key)

    pass

def update():
    for object in world_all:
        object.update()

    pass

def late_update():
    global collision

    for object in world_all:
        object.late_update()

    collision.all_collision()
    pass


def render_world():
    clear_canvas()

    for object in world_all:
        object.render()

    update_canvas()
    pass

def level_changer(): # level change

    pass



open_canvas()
initialize()

running = True





# Game Loop~
while running:

    handle_events()
    update()
    late_update()
    render_world()

    delay(0.01)

close_canvas()