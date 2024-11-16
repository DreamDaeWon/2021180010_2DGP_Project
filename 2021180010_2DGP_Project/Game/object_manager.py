from dw_define import*

world = [[],[],[],[]] # 모든 세상 객체들 # 0번 배경, 1번 보스, 2번 플레이어, 3번 총알

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

    pass

