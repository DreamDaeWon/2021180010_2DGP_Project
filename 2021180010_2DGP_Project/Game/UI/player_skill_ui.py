import math

from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime


class Player_Skill_Ui:
    image = None
    def __init__(self,x):
        self.this_delete = False

        self.x = 100*x - 30
        self.y = 630

        self.image_width = 0
        self.image_height = 0

        self.now_image = 0

        self.init_image()

    def init_image(self):
        if Player_Skill_Ui.image is None:
            path = 'UI/resource/player_skill_ui.png'  # main.py 기준임
            Player_Skill_Ui.image = load_image(path)

        self.now_image = Player_Skill_Ui.image


        pass

    def update(self):
        self.image_width = self.now_image.w
        self.image_height = self.now_image.h

        pass

    def late_update(self):
        pass


    def render(self):
        self.now_image.draw(self.x,self.y,self.image_width * 0.3,self.image_height * 0.3)
        pass
    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        #return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry
        pass
