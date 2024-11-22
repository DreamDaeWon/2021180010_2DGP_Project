import object_manager
from Game.CupHeadBanging.cupheadBanging import CupheadBanging
from Game.UI.back_ground_Farm import Back_Ground_Farm
from Game.collision import World_collision



def change_stage(want_level_num):
    object_manager.delete_all()

    if want_level_num == 1:
        object_manager.world[object_manager.back_ground_list_num].append(Back_Ground_Farm())

        # Player 추가
        object_manager.world[2].append(CupheadBanging(1))
        World_collision.get_player(object_manager.world[2][0])
        pass

    if want_level_num == 2:
        object_manager.world[2].append(CupheadBanging(2))
        pass

    pass