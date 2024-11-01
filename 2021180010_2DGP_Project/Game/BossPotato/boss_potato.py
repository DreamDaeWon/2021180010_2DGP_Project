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
