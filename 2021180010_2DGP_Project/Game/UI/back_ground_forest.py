import math

import pico2d
from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime
import object_manager


class Back_Ground_Forest:
    image_far = None
    image_middle = None
    image_ground = None
    image_water = None

    def __init__(self):
        self.this_delete = False

        self.x = 1400 * 0.5
        self.y = 700 * 0.5

        self.image_width = 1100
        self.image_height = 700

        self.far_image = 0

        self.middle_image = 0

        self.image_ground = 0

        self.image_water = 0


        self.frame = 0.0
        self.frame_speed = 20.0

        self.moveX = 0.0
        self.moveY = 0.0



        self.init_image()

    def init_image(self):
        if Back_Ground_Forest.image_far is None:
            path = 'Resources/UiResources/back_ground_forest_resources/far_forest.png'  # main.py 기준임
            Back_Ground_Forest.image_far = load_image(path)

        self.far_image = Back_Ground_Forest.image_far


        if Back_Ground_Forest.image_middle is None:
            path = 'Resources/UiResources/back_ground_forest_resources/middle_forest.png'  # main.py 기준임
            Back_Ground_Forest.middle_image = load_image(path)

        self.middle_image = Back_Ground_Forest.middle_image


        if Back_Ground_Forest.image_ground is None:
            path = 'Resources/UiResources/back_ground_forest_resources/forest_ground.png'
            Back_Ground_Forest.image_ground = load_image(path)

        self.image_ground = Back_Ground_Forest.image_ground


        if Back_Ground_Forest.image_water is None:
            Back_Ground_Forest.image_water = []

            path = 'Resources/UiResources/back_ground_forest_resources/water/slime_bg_stream_'

            for a in range(1,13):
                finalpath = path + str(a) + '.png'
                Back_Ground_Forest.image_water.append(load_image(finalpath))

        self.image_water = Back_Ground_Forest.image_water

        pass

    def update(self):

        if self.frame <= 11:
            self.frame += self.frame_speed * frametime.frame_time
        else:
            self.frame = 0.0

        if object_manager.world[object_manager.player_list_num][0] is None:
            return

        self.moveX = -object_manager.world[object_manager.player_list_num][0].CX * 0.25

        pass

    def late_update(self):
        pass


    def render(self):
        self.far_image.draw(self.x + self.moveX * 0.5 *0.5,self.y + 130, self.far_image.w, self.far_image.h)

        self.middle_image.draw(self.x + self.moveX * 0.7,self.y + 125,self.middle_image.w, self.middle_image.h)

        self.image_ground.draw(self.x + self.moveX,self.y - 70,self.image_ground.w, self.image_ground.h)

        self.image_water[int(self.frame)].clip_composite_draw(0,0, self.image_water[int(self.frame)].w, self.image_water[int(self.frame)].h,
                                                              0,'',self.x + 95 + self.moveX * 0.7,self.y - 65)
        #pico2d.Image.clip_composite_draw(self.x,self.y,self.image_width,self.image_height)


        pass
    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        #return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry
        pass
