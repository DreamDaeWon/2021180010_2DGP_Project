import math

from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime


class Back_Ground_Farm:
    image = None
    def __init__(self):
        self.this_delete = False

        self.x = 1100 * 0.5
        self.y = 700 * 0.5

        self.image_width = 1100
        self.image_height = 700

        self.now_image = 0

        self.bgm = load_music('Resources/music/Cuphead OST - Botanic Panic [Music].mp3')

        self.bgm.set_volume(25)

        self.bgm.repeat_play()

        self.init_image()

    def init_image(self):
        if Back_Ground_Farm.image is None:
            path = 'Resources/UiResources/farm.png'  # main.py 기준임
            Back_Ground_Farm.image = load_image(path)

        self.now_image = Back_Ground_Farm.image


        pass

    def update(self):


        pass

    def late_update(self):
        pass


    def render(self):
        self.now_image.draw(self.x,self.y,self.image_width,self.image_height)
        pass
    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        #return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry
        pass
