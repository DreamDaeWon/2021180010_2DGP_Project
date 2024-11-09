import enum

import math

from pico2d import*



class Boss_Potato:

    def __init__(self):

        self.CX = 100

        self.CY = 300

        self.frame = 0

        self.in_put_resources()

        # 움직임 관련 변수
        # 달리기
        self.running = False
        self.rundir = 0
        self.run_speed = 10

        self.before_state_tuple = 0
        self.now_state_tuple = 0

        self.image = 0


        # 상태에 따른 튜플
        self.Idle = []

        self.Create = []

        self.now_state_tuple = self.Create

    pass


    def in_put_resources(self):
        # 리소스 기본상태
        path = 'BossPotato/PotatoResource/BossPotato.png'  # main.py 기준임
        self.image = load_image(path)

        # 한 사진당 가로크기, 세로크기, 총 몇 프레임인지?, x값 어디서부터 시작하는지?, y값 어디서부터 시작하는지?, x값 얼마만큼 떨어지는지? , y값 얼마만큼 떨어지는지?
        self.Idle = [526,512,20,7,4522,8,6]
        self.Create = [526,512,20,7,4522,8,6]

    def boss_state_update(self):  # 보스 상태가 변경 될 때 해주 어야 할 것들
        if self.before_state_tuple != self.now_state_tuple:
            self.frame = 0
            pass


    def boss_move(self):
        pass





    def boss_resource_state(self):

        self.before_state_tuple = self.now_state_tuple

        #self.now_state_tuple = self.Create

        if self.before_state_tuple == self.now_state_tuple:
            self.frame += 1 * self.now_state_tuple[1]
            if self.frame >= self.now_state_tuple[0]:
                self.frame = 0
        else:
            self.boss_state_update()
            print('in this')



        pass

