from dw_define import*

world = [[],[],[]] # 모든 세상 객체들

def input_object(object,list):
    world[list].append(object)
    pass

def delete_object(object):
    for list in world:
        for i in list:
            if i == object:
                world.remove(object)
                del i

    pass

