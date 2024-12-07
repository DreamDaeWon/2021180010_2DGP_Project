import object_manager
from Game.CupHeadBanging.cupheadBanging import CupheadBanging
from Game.UI.back_ground_Farm import Back_Ground_Farm
from Game.UI.back_ground_forest import Back_Ground_Forest
from Game.collision import World_collision
from Game.UI.Title.ui_main_title import Ui_Main_Title



def change_stage(want_level_num):
    object_manager.delete_all()

    World_collision.boss = None

    if want_level_num == 0:
        object_manager.world[object_manager.back_ground_list_num].append(Ui_Main_Title())

    if want_level_num == 1:
        object_manager.world[object_manager.back_ground_list_num].append(Back_Ground_Farm())

        # Player 추가
        object_manager.world[2].append(CupheadBanging(1))
        World_collision.get_player(object_manager.world[2][0])
        pass

    if want_level_num == 2:
        object_manager.world[object_manager.back_ground_list_num].append(Back_Ground_Forest())
        object_manager.world[2].append(CupheadBanging(2))
        World_collision.get_player(object_manager.world[2][0])
        pass

    pass