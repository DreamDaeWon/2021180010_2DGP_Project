import math

from pico2d import*

import os
import sys

import object_manager

# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime


class Ui_Black_Circle:
    image = None
    def __init__(self):
        self.this_delete = False

        self.x = 1100 * 0.5
        self.y = 700 * 0.5

        self.image_width = 6600
        self.image_height = 4200

        self.now_size = 5.0



        self.now_image = 0

        self.init_image()

    def init_image(self):
        if Ui_Black_Circle.image is None:
            path = 'UI/resource/Black_Circle.png'  # main.py 기준임
            Ui_Black_Circle.image = load_image(path)

        self.now_image = Ui_Black_Circle.image


        pass

    def update(self):
        if self.now_size > 0.3:
            self.now_size -= frametime.frame_time * 1.5

        pass

    def late_update(self):

        if object_manager.world[object_manager.player_list_num][0] is None:
            self.this_delete = True

        else:
            self.x = object_manager.world[object_manager.player_list_num][0].CX
            self.y = object_manager.world[object_manager.player_list_num][0].CY


        pass


    def render(self):
        self.now_image.clip_composite_draw(0,0,self.image_width,self.image_height,0,'',self.x,self.y,self.image_width * self.now_size ,self.image_height *  self.now_size )

        pass
    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        #return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry
        pass
