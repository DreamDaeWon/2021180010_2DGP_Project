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


class UI_End:
    image_ko = None

    def __init__(self):
        self.this_delete = False

        self.x = 1400 * 0.5
        self.y = 700 * 0.5

        self.bgm = load_music('Resources/music/sound_effect/cuphead-a-knockout-sound.mp3')

        self.bgm.set_volume(128)

        self.bgm.play(1)

        self.back_ground_image = load_image('Resources/UiResources/black.png')

        self.image_width = 1100
        self.image_height = 700

        self.image_find_cookie = 0
        self.image_drop_cookie = 0

        self.max_frame_find_cookie = 11
        self.max_frame_drop_cookie = 30

        self.frame = 0.0

        self.frame_speed = 10.0

        self.bool_cookie = False

        self.moveX = 0.0
        self.moveY = 0.0

        self.story_font = load_font('Resources/Font/cuphead_font_by_ripoof_dept3h3.ttf', 50)

        self.story_font_Two = load_font('Resources/Font/cuphead_font_by_ripoof_dept3h3.ttf', 30)



        self.init_image()

    def init_image(self):
        self.image_drop_cookie = []

        path = 'Resources/PlayerResoures/Drop Cookie/cuphead_intro_no_cookie_'  # main.py 기준임
        for a in range(1, 30 + 1):
            finalpath = path + str(a) + '.png'
            self.image_drop_cookie.append(load_image(finalpath))
        pass


    def update(self):

        if self.frame <= self.max_frame_drop_cookie:
            self.frame += self.frame_speed * frametime.frame_time

        if self.bool_cookie is False:
            self.frame = 0
        else:
            if self.frame >= self.max_frame_drop_cookie:
                self.frame = 0


        pass

    def late_update(self):
        pass


    def render(self):

        self.back_ground_image.draw(0,0)

        self.image_drop_cookie[int(self.frame)].clip_composite_draw(0,0, self.image_drop_cookie[int(self.frame)].w,
                                                           self.image_drop_cookie[int(self.frame)].h,
                                                              0,'',550,100)

        if self.bool_cookie is False:
            self.story_font.draw(100,600,'Finally we made cookies!',(255,255,255))
            self.story_font.draw(150,500,'Then, should I try it?',(255,255,255))
            self.story_font_Two.draw(300,400,'push b',(255,255,255))


        pass
    def key_input_down(self, Key):
        if Key == SDLK_b:
            self.bool_cookie = True
        pass

    def key_input_up(self, Key):
        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        #return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry
        pass