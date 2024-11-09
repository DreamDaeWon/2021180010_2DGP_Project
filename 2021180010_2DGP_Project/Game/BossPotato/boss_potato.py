import enum

import math

from pico2d import*



class Boss_Potato:

    def __init__(self):

        self.CX = 600

        self.CY = 400

        self.frame = 0 # 그냥 프레임 (열 프레임)

        self.row_frame = 0 # 행 프레임

        self.in_put_resources()

        # 움직임 관련 변수
        # 달리기
        self.running = False
        self.rundir = 0
        self.run_speed = 10

        self.before_state_tuple = 0
        self.now_state_dict = 0

        #self.image = 0


        # 상태에 따른 딕셔너리
        self.Idle = []

        self.Create = {}

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
        self.Create['rx'] = 526 # 가로크기
        self.Create['ry'] = 512 # 세로크기
        self.Create['frame'] = 20 # 총 몇 프레임인지?
        self.Create['frame_speed'] = 0.5  # 프레임 속도
        self.Create['row_frame'] = 6 # 가로 프레임 몇 개인지?
        self.Create['column_frame'] = 4 # 세로 프레임 몇 개인지?
        self.Create['last_row_frame'] = 2 # 마지막 줄 가로 프레임
        self.Create['left'] = 7 # x값 어디서부터 시작하는지?
        self.Create['bottom'] = 4522 # y값 어디서부터 시작하는지?
        self.Create['go_right'] = 8 # x값 얼마만큼 떨어지는지?
        self.Create['go_down'] = 6 # y값 얼마만큼 떨어지는지?


    def boss_state_update(self):  # 보스 상태가 변경 될 때 해주 어야 할 것들
        if self.before_state_tuple != self.now_state_dict:
            self.frame = 0
            pass


    def boss_move(self):
        pass

    def render(self):
        self.image.clip_composite_draw(self.now_state_dict['left'], self.now_state_dict['bottom'], self.now_state_dict['bottom'],)
        pass

    def boss_resource_state(self):

        self.before_state_tuple = self.now_state_dict

        #self.now_state_dict = self.Create

        if self.before_state_tuple == self.now_state_dict:
            self.frame += 1 * self.now_state_dict[1]
            if self.frame >= self.Create['column_frame'] and self.frame >= self.Create['last_row_frame']:
                self.frame = 0
                self.row_frame = 0
        else:
            self.boss_state_update()
            print('in this')



        pass

