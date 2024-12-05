import enum

import math

import random

import pygame
from pico2d import*

import os
import sys

#from Game.BossPotato.boss_potato_skill import Boss_potato_skill

#from Game.BossPotato.boss_potato_skill_item import Boss_potato_skill_item

from Game.collision import World_collision


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime
import object_manager



class Boss_Blue_One_Phase:
    Boss_image_Intro = None
    Boss_image_idle = None
    Boss_image_Jump = None
    Boss_image_Punch = None
    Boss_image_Question_player_item = None
    Boss_image_Change_Phase = None
    def __init__(self):


        self.this_delete = False # 이 객체를 지워야 하는지?


        self.CX = 850

        self.RealCX = 850

        self.CY = 0

        self.LR = False

        self.Boss_Size = 1.0


        self.boss_blue_rx = 100.0

        self.boss_blue_ry = 100.0

        self.frame = 0 # 그냥 프레임 (열 프레임)

        self.row_frame = 0 # 행 프레임

        self.frame_move = 1 # 프레임 진행방향 1 이면 그냥 재생, -1 이면 역재생

        self.hp = 1

        self.hit_bool = False


        self.moveX = 0.0



        self.intro_ground_frame = 0 # 그냥 프레임 (열 프레임)

        self.intro_ground_row_frame = 0 # 행 프레임


        self.boss_size = 1.0

        # 움직임 관련 변수



        #self.image = 0

        self.shoot = False # 쐈는지?

        self.player = object_manager.world[2][0]


        # 상태에 따른 딕셔너리
        self.image_Intro = 0
        self.image_Jump  = 0
        self.image_Punch = 0
        self.image_Question_player_item = 0
        self.image_Change_Phase = 0


        self.in_put_resources()

        # 각 상태에 대한 구조체 정의 [프레임 개수, 프레임 속도, 이미지 배열]
        self.Intro = [27, 13, self.image_Intro]
        self.Punch = [16, 15, self.image_Punch]
        self.jump = [9, 15, self.image_Jump]
        self.Question_player_item = [37, 15, self.image_Question_player_item]
        self.Die = [48, 15, self.image_Change_Phase]




        self.now_state_tuple = self.Intro
        self.before_state_tuple = 0


    pass


    def in_put_resources(self):
        # 리소스 기본상태

        self.set_player_item_motion()
        self.set_intro_motion()
        self.set_jump_motion()
        self.set_punch_motion()
        self.set_die_motion()

        pass

    def set_intro_motion(self):
        # 보스 intro 모션
        if Boss_Blue_One_Phase.Boss_image_Intro is None:
            Boss_Blue_One_Phase.Boss_image_Intro = []

            path = 'Resources/Blue_Boss/Phase 1/Intro/slime_intro_'  # main.py 기준임

            for a in range(1, 27 + 1):
                finalPath = path + str(a) + '.png'
                Boss_Blue_One_Phase.Boss_image_Intro.append(load_image(finalPath))

        self.image_Intro = []
        self.image_Intro = Boss_Blue_One_Phase.Boss_image_Intro
        pass


    def set_punch_motion(self):
        # 보스 Punch 모션
        if Boss_Blue_One_Phase.Boss_image_Punch is None:
            Boss_Blue_One_Phase.Boss_image_Punch = []

            path = 'Resources/Blue_Boss/Phase 1/Punch/slime_punch_'  # main.py 기준임

            for a in range(1, 16 + 1):
                finalPath = path + str(a) + '.png'
                Boss_Blue_One_Phase.Boss_image_Punch.append(load_image(finalPath))

        self.image_Punch = []
        self.image_Punch = Boss_Blue_One_Phase.Boss_image_Punch
        pass

    def set_jump_motion(self):
        # 보스 Jump 모션
        if Boss_Blue_One_Phase.Boss_image_Jump is None:
            Boss_Blue_One_Phase.Boss_image_Jump = []

            path = 'Resources/Blue_Boss/Phase 1/Jump/slime_jump_000'  # main.py 기준임

            for a in range(1, 9 + 1):
                finalPath = path + str(a) + '.png'
                Boss_Blue_One_Phase.Boss_image_Jump.append(load_image(finalPath))

        self.image_Jump = []
        self.image_Jump = Boss_Blue_One_Phase.Boss_image_Jump
        pass

    def set_player_item_motion(self):
        # 보스 Question 모션
        if Boss_Blue_One_Phase.Boss_image_Question_player_item is None:
            Boss_Blue_One_Phase.Boss_image_Question_player_item = []

            path = 'Resources/Blue_Boss/Phase 1/Transition To Ph2/slime_morph_'  # main.py 기준임

            for a in range(1, 37 + 1):
                finalPath = path + str(a) + '.png'
                Boss_Blue_One_Phase.Boss_image_Question_player_item.append(load_image(finalPath))

        self.image_Question_player_item = []
        self.image_Question_player_item = Boss_Blue_One_Phase.Boss_image_Question_player_item
        pass

    def set_die_motion(self):
        # 보스 Change_Phase 모션
        if Boss_Blue_One_Phase.Boss_image_Change_Phase is None:
            Boss_Blue_One_Phase.Boss_image_Change_Phase = []

            path = 'Resources/Blue_Boss/Phase 1/Transition To Ph2/slime_morph_'  # main.py 기준임

            for a in range(1, 48 + 1):
                finalPath = path + str(a) + '.png'
                Boss_Blue_One_Phase.Boss_image_Change_Phase.append(load_image(finalPath))

        self.image_Change_Phase = []
        self.image_Change_Phase = Boss_Blue_One_Phase.Boss_image_Change_Phase
        pass


    def boss_state_update(self):  # 보스 상태가 변경 될 때 해주 어야 할 것들
        if self.before_state_tuple != self.now_state_tuple:
            self.frame = 0
            pass


    def boss_move(self):


        pass

    def update(self):

        self.boss_resource_state()

        self.moveX = object_manager.world[object_manager.back_ground_list_num][0].moveX

        self.CX = self.RealCX + self.moveX

        #self.boss_move()

        #self.boss_blue_rx = self.now_state_tuple[2][int(self.frame)].w * 0.5
        #self.boss_blue_ry = self.now_state_tuple[2][int(self.frame)].h * 0.5


        pass

    def late_update(self):
        World_collision.boss_blue_collision()
        #World_collision.player_skill_collision()
        pass

    def render(self):
        if self.LR is True:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0, 0, self.now_state_tuple[2][int(self.frame)].w, self.now_state_tuple[2][int(self.frame)].h,
                                                                         0,
                                                                         'h',
                                                                         self.CX - self.now_state_tuple[2][int(self.frame)].w * 0.5,
                                                                         self.CY + self.now_state_tuple[2][int(self.frame)].h * 0.5,
                                                                         self.now_state_tuple[2][int(self.frame)].w * self.Boss_Size,
                                                                         self.now_state_tuple[2][int(self.frame)].h * self.Boss_Size)
        else:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0, 0,
                                                                         self.now_state_tuple[2][int(self.frame)].w,
                                                                         self.now_state_tuple[2][int(self.frame)].h,
                                                                         0,
                                                                         '',
                                                                         self.CX - self.now_state_tuple[2][int(self.frame)].w * 0.5,
                                                                         self.CY + self.now_state_tuple[2][int(self.frame)].h * 0.5,
                                                                         self.now_state_tuple[2][
                                                                             int(self.frame)].w * self.Boss_Size,
                                                                         self.now_state_tuple[2][
                                                                             int(self.frame)].h * self.Boss_Size)


        pico2d.draw_rectangle(self.get_collision_size()[0],self.get_collision_size()[1],self.get_collision_size()[2],self.get_collision_size()[3])
        pass


    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass

    def boss_resource_state(self):

        self.before_state_tuple = self.now_state_tuple

        #self.now_state_tuple = self.Create

        if self.hp <= 0:
            self.now_state_tuple = self.Die

        if self.before_state_tuple == self.now_state_tuple:
            self.frame += 1 * self.now_state_tuple[1] * frametime.frame_time

            # 이건 인트로 때만 동작
            if self.now_state_tuple == self:
                if self.intro_ground_frame < 8:
                    self.frame = 0
                    self.row_frame = 0


            if self.frame >= self.now_state_tuple[0]:
                if self.now_state_tuple == self.Die:
                    self.this_delete = True
                elif self.now_state_tuple == self.Question_player_item:
                    self.frame = 35
                else:
                    self.frame = 0
                # 여기서 처음모션에서 아이들 모션으로 바꾸어 줌 # 인트로 때만 동작
                if self.now_state_tuple == self.Intro:
                    self.now_state_tuple = self.Punch # 일단은 반복
        else:
            self.boss_state_update()
            print('in this')



        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX  - self.boss_blue_rx * 2 , self.CY + self.boss_blue_ry * 2, self.CX, self.CY


    def shoot_skill(self):

        pass