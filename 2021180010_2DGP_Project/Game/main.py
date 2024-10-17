from pico2d import*

from CupHeadBanging.cupheadBanging import CupheadBainging

from Game.CupHeadBanging.cupheadBanging import CupheadBainging


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def initialize():
    global world_all
    world_all = []
    world_all.append(CupheadBainging());

    pass

def update():
    pass

def late_update():
    pass


def render_world():
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