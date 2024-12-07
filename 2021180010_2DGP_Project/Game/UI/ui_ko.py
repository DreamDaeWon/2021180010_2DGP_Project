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


class UI_Ko:
    image_ko = None

    def __init__(self):
        self.this_delete = False

        self.x = 1400 * 0.5
        self.y = 700 * 0.5

        self.bgm = load_music('Resources/music/sound_effect/cuphead-a-knockout-sound.mp3')

        self.bgm.set_volume(128)

        self.bgm.play(1)

        self.image_width = 1100
        self.image_height = 700

        self.ko_image = 0

        self.frame = 0.0
        self.max_frame = 27
        self.frame_speed = 10.0

        self.moveX = 0.0
        self.moveY = 0.0



        self.init_image()

    def init_image(self):
        if UI_Ko.image_ko is None:
            UI_Ko.image_ko = []

            path = 'Resources/UiResources/Knouck_Out/Knouck_out_'  # main.py 기준임
            for a in range(1,27 + 1):
                finalpath = path + str(a) + '.png'
                UI_Ko.image_ko.append(load_image(finalpath))

        self.ko_image = UI_Ko.image_ko

        pass

    def update(self):

        if self.frame <= 27:
            self.frame += self.frame_speed * frametime.frame_time

        if self.frame >= 27:
            self.frame = 0
            self.this_delete = True

        pass

    def late_update(self):
        pass


    def render(self):
        self.ko_image[int(self.frame)].clip_composite_draw(0,0, self.ko_image[int(self.frame)].w,
                                                           self.ko_image[int(self.frame)].h,
                                                              0,'',550,350,1100,700)


        pass
    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        #return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry
        pass
