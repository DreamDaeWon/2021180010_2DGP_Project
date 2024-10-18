from os import closerange

from dw_define import*

from CupHeadBanging.cupheadBanging import CupheadBainging



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                key_input(SDLK_RIGHT)
                pass
            elif event.key == SDLK_LEFT:
                key_input(SDLK_LEFT)
                pass
            elif event.key == SDLK_SPACE:
                key_input(SDLK_SPACE)
                pass


    pass


def initialize():
    global world_all
    world_all = []
    world_all.append(CupheadBainging());

    pass

def key_input(Key):
    for object in world_all:
        object.key_input(Key)

    pass

def update():
    for object in world_all:
        object.update()

    pass

def late_update():
    for object in world_all:
        object.late_update()
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