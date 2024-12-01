from dw_define import*

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

def delete_want_list_last_object(list_num):
    w = world[list_num]
    o = w[-1]
    w.pop()

    del o

def delete_object():
    for list in world:
        copy_list = list
        for i in copy_list:
            if i.this_delete:
                list.remove(i)
                del i

def delete_want_list(list_num):
    w = world[list_num]
    for i in w:
        del i
    w.clear()

def delete_all():
    for w in world:
        for i in w:
            del i
        w.clear()