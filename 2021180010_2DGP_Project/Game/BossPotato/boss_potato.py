import enum

import math

from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime


class Boss_Potato:

    def __init__(self):

        self.CX = 600

        self.CY = 100

        self.boss_potato_rx = 0.0

        self.boss_potato_ry = 0.0

        self.frame = 0 # 그냥 프레임 (열 프레임)

        self.row_frame = 0 # 행 프레임

        self.boss_size = 0.3

        # 움직임 관련 변수

        self.before_state_dict = 0
        self.now_state_dict = 0

        #self.image = 0


        # 상태에 따른 딕셔너리
        self.Idle = []

        self.Create = {}

        self.in_put_resources()

        self.now_state_dict = self.Create

    pass


    def in_put_resources(self):
        # 리소스 기본상태
        path = 'BossPotato/PotatoResource/BossPotato.png'  # main.py 기준임
        self.image = load_image(path)

        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?
        #self.Idle = [526,512,20,7,4522,8,6]

        self.set_in_game_motion()




    def set_in_game_motion(self):
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?
        # self.Idle = [526,512,20,7,4522,8,6]
        self.Create['width'] = 526  # 가로크기
        self.Create['high'] = 512  # 세로크기
        self.Create['frame'] = 20  # 총 몇 프레임인지?
        self.Create['frame_speed'] = 5  # 프레임 속도
        self.Create['column_frame'] = 6  # 가로 프레임 몇 개인지?
        self.Create['row_frame'] = 4  # 세로 프레임 몇 개인지?
        self.Create['last_row_frame'] = 2  # 마지막 줄 가로 프레임
        self.Create['left'] = 7  # x값 어디서부터 시작하는지?
        self.Create['bottom'] = 4522  # y값 어디서부터 시작하는지?
        self.Create['go_right'] = 531  # x값 얼마만큼 떨어지는지?
        self.Create['go_down'] = 517  # y값 얼마만큼 떨어지는지?
        pass


    def boss_state_update(self):  # 보스 상태가 변경 될 때 해주 어야 할 것들
        if self.before_state_dict != self.now_state_dict:
            self.frame = 0
            pass


    def boss_move(self):
        pass

    def update(self):

        self.boss_resource_state()

        self.boss_move()

        self.boss_potato_rx =  self.now_state_dict['width'] * 0.5 * self.boss_size
        self.boss_potato_ry = self.now_state_dict['high'] * 0.5 * self.boss_size


        pass

    def late_update(self):

        pass

    def render(self):
        self.image.clip_composite_draw(int(self.now_state_dict['left'] + (self.now_state_dict['go_right'] * int(int(self.frame) % self.now_state_dict['column_frame']))),
                                       int(self.now_state_dict['bottom'] - (self.now_state_dict['go_down'] * self.row_frame)),
                                       self.now_state_dict['width'],
                                       self.now_state_dict['high'],0,'',self.CX,self.CY,
                                       self.now_state_dict['width'] * self.boss_size,self.now_state_dict['high'] * self.boss_size)

        pico2d.draw_rectangle(self.get_collision_size()[0],self.get_collision_size()[1],self.get_collision_size()[2],self.get_collision_size()[3])
        pass


    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass

    def boss_resource_state(self):

        self.before_state_dict = self.now_state_dict

        #self.now_state_dict = self.Create

        if self.before_state_dict == self.now_state_dict:
            self.frame += 1 * self.now_state_dict['frame_speed'] * frametime.frame_time
            self.row_frame = int(self.frame / self.now_state_dict['column_frame'])
            if self.frame >= self.now_state_dict['frame']:

                # 여기서 처음모션에서 아이들 모션으로 바꾸어 줌
                if self.now_state_dict == self.Create:
                    self.now_state_dict = self.Create # 일단은 반복

                self.frame = 0
                self.row_frame = 0
        else:
            self.boss_state_update()
            print('in this')



        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX - self.boss_potato_rx, self.CY + self.boss_potato_ry, self.CX + self.boss_potato_rx, self.CY - self.boss_potato_ry