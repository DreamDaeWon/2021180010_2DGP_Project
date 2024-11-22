from dw_define import*

from Game.collision import World_collision

world = [[],[],[],[],[],[],[],[]] # 모든 세상 객체들 # 0번 배경, 1번 보스, 2번 플레이어, 3번 보스 스킬, 4번 플레이어 스킬, 5번 플레이어 아이템, 6번 이펙트, 7번 UI

back_ground_list_num = 0

boss_list_num = 1

player_list_num = 2

boss_skill_list_num = 3

player_skill_list_num = 4

player_skill_item_num = 5

effect_num = 6

UI_list_num = 7


def input_object(object,list):
    world[list].append(object)
    pass

def delete_want_object(object):
    for list in world:
        for i in list:
            if i == object:
                world.remove(object)
                del i


def delete_object():

    for list in world:
        copy_list = list
        for i in copy_list:
            if i.this_delete:
                list.remove(i)

def change_object(want_level_num):

    if want_level_num == 1:
        object_manager.world[object_manager.back_ground_list_num].append(Back_Ground_Farm())

        # Player 추가
        object_manager.world[2].append(CupheadBanging())
        World_collision.get_player(object_manager.world[2][0])
        pass

    if want_level_num == 2:
        pass

    pass

