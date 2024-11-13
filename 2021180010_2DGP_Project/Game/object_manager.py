from dw_define import*

world = [] # 모든 세상 객체들

def input_object(object):
    world.append(object)
    pass

def delete_object(object):
    for i in world:
        if i == object:
            world.remove(object)
    pass

