from os import closerange

from Game import stage_manager
from dw_define import*

from Game.collision import World_collision



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
    #global world_all
    #world_all = [[],[],[],[]] # 0번 배경, 1번 보스, 2번 플레이어, 3번 총알
# 추가 순서는 배경->보스->플레이어 순
    #배경 추가
    #object_manager.world[object_manager.back_ground_list_num].append(Back_Ground_Farm())
#
#
    ## Player 추가
    #object_manager.world[2].append(CupheadBanging())
    #World_collision.get_player(object_manager.world[2][0])


    # 스테이지 매니저 추가
    stage_manager.change_stage(0)



    pass

def key_input_down(Key):

    for world in object_manager.world:
        for object in world:
            object.key_input_down(Key)

    pass

def key_input_up(Key):
    for world in object_manager.world:
        for object in world:
            object.key_input_up(Key)

    pass

def update():
    for world in object_manager.world:
        for object in world:
            object.update()

    pass

def late_update():
    for world in object_manager.world:
        for object in world:
            object.late_update()

    World_collision.all_collision()

    object_manager.delete_object()
    pass


def render_world():
    clear_canvas()

    for world in object_manager.world:
        for object in world:
            object.render()

    update_canvas()
    pass

def level_changer(): # level change

    pass



open_canvas(1100,700)
initialize()

running = True

# Game Loop~
while running:

    frametime.current_time = time.time()

    handle_events()
    update()
    late_update()
    render_world()

    frametime.frame_time = time.time() - frametime.current_time
    frame_rate = 1.0 / frametime.frame_time
    frametime.current_time += frametime.frame_time

    #delay(0.01)

close_canvas()