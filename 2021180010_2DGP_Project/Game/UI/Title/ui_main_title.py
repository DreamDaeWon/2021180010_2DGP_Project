import math

from pico2d import*

import os
import sys

import object_manager

import stage_manager

# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime


class Ui_Main_Title:
    mian_image = None
    black_circle = None
    banging = None
    made_by_dw = None
    main_cuphead_banging = None

    def __init__(self):
        self.this_delete = False

        self.x = 1100 * 0.5
        self.y = 700 * 0.5


        self.image_width = 6600
        self.image_height = 4200

        self.now_size = 5.0


        self.bRender_Restart_Message_UI = False


        self.mian_image = 0

        self.black_circle = 0

        self.banging = 0

        self.made_by_dw = 0

        self.main_cuphead_banging = []

        self.init_image()


    def init_image(self):
        if Ui_Main_Title.mian_image is None:
            path = 'UI/resource/Title/title_screen_background.png'  # main.py 기준임
            Ui_Main_Title.mian_image = load_image(path)

        self.mian_image = Ui_Main_Title.mian_image

        if Ui_Main_Title.black_circle is None:
            path = 'UI/resource/Black_Circle.png'  # main.py 기준임
            Ui_Main_Title.black_circle = load_image(path)

        self.black_circle = Ui_Main_Title.black_circle

        if Ui_Main_Title.banging is None:
            path = 'UI/resource/Title/Title_Banging.png'  # main.py 기준임
            Ui_Main_Title.banging = load_image(path)

        self.banging = Ui_Main_Title.banging

        if Ui_Main_Title.made_by_dw is None:
            path = 'UI/resource/Title/made_by_dw.png'  # main.py 기준임
            Ui_Main_Title.made_by_dw = load_image(path)

        self.made_by_dw = Ui_Main_Title.made_by_dw

        if Ui_Main_Title.main_cuphead_banging is None:
            path = 'UI/resource/Title/Cup_Head_Banging_Title'  # main.py 기준임
            Ui_Main_Title.main_cuphead_banging = []
            for i in range(1,13):
                finalpath = path + str(i) + '.png'
                Ui_Main_Title.main_cuphead_banging.append(load_image(finalpath))

        self.main_cuphead_banging = Ui_Main_Title.main_cuphead_banging

        pass

    def update(self):
        if self.now_size > 0.32:
            self.now_size -= frametime.frame_time * 1.5
        else:
            self.bRender_Restart_Message_UI = True

        pass

    def late_update(self):

        if object_manager.world[object_manager.player_list_num][0] is None:
            self.this_delete = True


        pass


    def render(self):

        self.now_image.clip_composite_draw(0,0,self.image_width,self.image_height,0,'',self.x,self.y,self.image_width * self.now_size ,self.image_height *  self.now_size )

        if self.bRender_Restart_Message_UI:
            self.Restart_Message_image.draw(550,350,1100,700)

        pass

    def key_input_down(self, Key):
        if Key == SDLK_KP_ENTER:
            if self.bRender_Restart_Message_UI:
                stage_manager.change_stage(1)
        pass

    def key_input_up(self, Key):
        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        #return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry
        pass
