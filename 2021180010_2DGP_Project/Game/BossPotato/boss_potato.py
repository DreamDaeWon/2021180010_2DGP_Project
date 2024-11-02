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

    pass


def in_put_resources(self):
        # 리소스 기본상태
    path = 'CupHeadBanging/PlayerResoures/Idle/cuphead_idle_000'  # main.py 기준임
    self.image_Idle = []
    for a in range(1, 8 + 1):
        finalPath = path + str(a) + '.png'
        self.image_Idle.append(load_image(finalPath))

def boss_state_updete(self):  # 보스 상태가 변경 될 때 해주 어야 할 것들
    if self.before_state_tuple != self.now_state_tuple:
        self.frame = 0
        pass






