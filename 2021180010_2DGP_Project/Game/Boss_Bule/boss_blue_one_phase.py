import enum

import math

import random
from math import radians

import pygame
from pico2d import*

import os
import sys

import random

import math

from pygame.pypm import FALSE

from Game.Boss_Bule.boss_blue_player_item import Boss_Blue_Player_Item

from Game.collision import World_collision, Collision

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

        self.jump_up = 3.0


        self.shoot_bool = False # 물음표 마크를 쐈는지?


        self.boss_blue_rx = 100.0

        self.boss_blue_ry = 100.0

        self.frame = 0 # 그냥 프레임 (열 프레임)

        self.row_frame = 0 # 행 프레임

        self.frame_move = 1 # 프레임 진행방향 1 이면 그냥 재생, -1 이면 역재생

        self.hp = 1

        self.hit_bool = False

        self.jumping = False

        self.jump_angle = 0.0

        self.gravity = 9.8

        self.setJump_Finish_Pos = 0.0

        self.setJump_start_pos = 0.0

        self.set_Player_Pos = False


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
        self.Punch = [16, 13, self.image_Punch]
        self.jump = [19, 19, self.image_Jump]
        self.Question_player_item = [37, 13, self.image_Question_player_item]
        self.Die = [48, 15, self.image_Change_Phase]

        self.All_State = [self.Punch,self.jump]

        self.all_skill_num = 0 # 몇 번 스킬을 사용하였는지?


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

            path = 'Resources/Blue_Boss/Phase 1/Jump/jump_'  # main.py 기준임

            for a in range(1, 19 + 1):
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
        self.boss_jump()
        self.boss_shoot_skill()

        pass

    def boss_shoot_skill(self):
        if self.now_state_tuple == self.Question_player_item and self.frame >= 34:
            if self.shoot_bool is False:
                self.shoot_skill()
                self.shoot_bool = True

        else:
            self.shoot_bool = False



        pass

    def boss_jump(self):

        if self.now_state_tuple == self.jump and int(self.frame) == 9:
            self.jumping = True

        if self.jumping is False:
            self.set_Player_Pos = False
            self.jump_angle = 0.0

        if self.jumping is True:

            if self.set_Player_Pos is False:
                self.setJump_Finish_Pos = object_manager.world[2][0].CX - self.moveX + self.boss_blue_rx
                self.setJump_start_pos = self.RealCX
                self.set_Player_Pos = True


            if self.jump_angle < 180.0:
                self.jump_angle += 200.0 * frametime.frame_time

            if self.jump_angle > 180.0:
                self.jump_angle = 180.0

            self.CY += math.cos(radians(self.jump_angle)) * self.jump_up
            t = self.jump_angle/180.0
            self.RealCX = (1-t) * self.setJump_start_pos + t * self.setJump_Finish_Pos


            pass

        pass

    def update(self):

        self.boss_resource_state()

        self.moveX = object_manager.world[object_manager.back_ground_list_num][0].moveX

        self.CX = self.RealCX + self.moveX

        self.boss_move()

        #self.boss_blue_rx = self.now_state_tuple[2][int(self.frame)].w * 0.5
        #self.boss_blue_ry = self.now_state_tuple[2][int(self.frame)].h * 0.5


        pass

    def late_update(self):
        World_collision.boss_blue_collision()
        #World_collision.player_skill_collision()
        self.skill_punch()
        pass

    def render(self):
        if self.LR is True:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0, 0, self.now_state_tuple[2][int(self.frame)].w,
                                                                         self.now_state_tuple[2][int(self.frame)].h,
                                                                         0,
                                                                         'h',
                                                                         self.CX + self.now_state_tuple[2][int(self.frame)].w * 0.5 - self.boss_blue_rx * 2,
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
        pico2d.draw_rectangle(self.get_punch_collision_size()[0],self.get_punch_collision_size()[1],self.get_punch_collision_size()[2],self.get_punch_collision_size()[3])
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
                elif self.now_state_tuple == self.jump and self.jumping:
                    self.frame = 18
                else:
                    self.frame = 0
                    if self.CX - self.boss_blue_rx > object_manager.world[2][0].CX:
                        self.LR = False
                    else:
                        self.LR = True
                    next_state = random.randint(0, 1)
                    self.now_state_tuple = self.All_State[next_state]
                    self.all_skill_num += 1

                    if self.all_skill_num is 2:
                        self.now_state_tuple = self.Question_player_item
                        self.all_skill_num = 0
                    #self.now_state_tuple = self.jump  # 일단은 반복

                # 여기서 처음모션에서 아이들 모션으로 바꾸어 줌 # 인트로 때만 동작
                if self.now_state_tuple == self.Intro:
                    if self.CX - self.boss_blue_rx > object_manager.world[2][0].CX:
                        self.LR = False
                    else:
                        self.LR = True
                    next_state = random.randint(0, 2)
                    self.now_state_tuple = self.All_State[next_state]
                    #self.now_state_tuple = self.jump # 일단은 반복
        else:
            self.boss_state_update()
            print('in this')



        pass


    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX  - self.boss_blue_rx * 2 , self.CY + self.boss_blue_ry * 2, self.CX, self.CY

    def get_punch_collision_size(self):
        # left, top ,right, bottom
        if self.LR is True:
            return self.CX - self.boss_blue_rx * 2, self.CY + self.boss_blue_ry * 4, self.CX + self.boss_blue_rx * 4, self.CY + self.boss_blue_ry * 1
        else:
            return self.CX - self.boss_blue_rx * 6, self.CY + self.boss_blue_ry * 4, self.CX, self.CY + self.boss_blue_ry * 1


    def skill_punch(self):
        if self.now_state_tuple == self.Punch:
            if self.frame >= 9 and self.frame <= 12:
                if Collision.box_collision(Collision,self.get_punch_collision_size(),object_manager.world[object_manager.player_list_num][0].get_collision_size()) is True:
                    object_manager.world[object_manager.player_list_num][0].hit_bool = True
                    print('good')

        pass


    def shoot_skill(self):
        for a in range(3):
            object_manager.world[object_manager.player_skill_item_num].append(Boss_Blue_Player_Item(-45 + 45 * a,1 - a))

        pass