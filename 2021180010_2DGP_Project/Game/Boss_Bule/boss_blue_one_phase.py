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

        self.CY = 300




        self.boss_potato_rx = 0.0

        self.boss_potato_ry = 0.0

        self.frame = 0 # 그냥 프레임 (열 프레임)

        self.row_frame = 0 # 행 프레임

        self.frame_move = 1 # 프레임 진행방향 1 이면 그냥 재생, -1 이면 역재생

        self.hp = 1

        self.hit_bool = False



        self.intro_ground_frame = 0 # 그냥 프레임 (열 프레임)

        self.intro_ground_row_frame = 0 # 행 프레임


        self.boss_size = 1.0

        # 움직임 관련 변수

        self.before_state_dict = 0
        self.now_state_dict = 0

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

        self.now_state_dict = self.Intro

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

        self.image_Idle = []
        self.image_Idle = Boss_Blue_One_Phase.Boss_image_Intro
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
        if self.before_state_dict != self.now_state_dict:
            self.frame = 0
            pass


    def boss_move(self):

        if int(self.frame) > 13:
            self.shoot = False

        if not self.shoot:
            if self.now_state_dict == self.attack_dict and int(self.frame) == 13:
                self.shoot_skill()
                self.shoot = True

        if self.hit_bool is True:
            if self.hp > 0:
                self.hp -= 1
            self.hit_bool = False

        pass

    def update(self):

        self.boss_resource_state()

        self.boss_move()

        self.boss_potato_rx =  self.now_state_dict['width'] * 0.5 * self.boss_size
        self.boss_potato_ry = self.now_state_dict['high'] * 0.5 * self.boss_size


        pass

    def late_update(self):
        World_collision.boss_collision()
        World_collision.player_skill_collision()
        pass

    def render(self):



        pico2d.draw_rectangle(self.get_collision_size()[0],self.get_collision_size()[1],self.get_collision_size()[2],self.get_collision_size()[3])
        pass


    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass

    def boss_resource_state(self):

        self.before_state_dict = self.now_state_dict

        #self.now_state_dict = self.Create

        if self.hp <= 0:
            self.now_state_dict = self.die_dict
            self.CY -= 50


        if self.now_state_dict == self.Create:
            self.intro_ground_frame += 1 * self.intro_ground_dict['frame_speed'] * frametime.frame_time
            self.intro_ground_row_frame = int(self.intro_ground_frame / self.intro_ground_dict['column_frame'])
            if self.frame >= self.now_state_dict['frame']:
                self.frame = 0
                self.row_frame = 0


        if self.before_state_dict == self.now_state_dict:
            self.frame += 1 * self.now_state_dict['frame_speed'] * frametime.frame_time * self.frame_move
            self.row_frame = int(self.frame / self.now_state_dict['column_frame'])




            # 이건 인트로 때만 동작
            if self.now_state_dict == self.Create:
                if self.intro_ground_frame < 8:
                    self.frame = 0
                    self.row_frame = 0

            if self.frame <= -1:
                self.frame_move = self.frame_move * -1
                self.frame = 0
                self.row_frame = 0


            if self.frame >= self.now_state_dict['frame']:
                # 여기서 처음모션에서 아이들 모션으로 바꾸어 줌 # 인트로 때만 동작
                if self.now_state_dict == self.Create:
                    self.now_state_dict = self.attack_dict # 일단은 반복

                if self.now_state_dict == self.die_dict:
                    self.frame_move = self.frame_move * -1
                    self.frame -= self.now_state_dict['frame_speed'] * frametime.frame_time * 1
                else:
                    self.frame = 0
                self.row_frame = 0
        else:
            self.boss_state_update()
            print('in this')



        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX - self.boss_potato_rx, self.CY + self.boss_potato_ry * 0.5, self.CX + self.boss_potato_rx, self.CY - self.boss_potato_ry


    def shoot_skill(self):

        pass