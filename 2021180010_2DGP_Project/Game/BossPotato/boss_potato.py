import enum

import math

import random

import pygame
from pico2d import*

import os
import sys

from Game.BossPotato.boss_potato_skill import Boss_potato_skill

from Game.BossPotato.boss_potato_skill_item import Boss_potato_skill_item

from Game.collision import World_collision


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime
import object_manager



class Boss_Potato:
    Boss_image = None
    def __init__(self):


        self.this_delete = False # 이 객체를 지워야 하는지?


        self.CX = 850

        self.CY = 300

        self.boss_potato_rx = 0.0

        self.boss_potato_ry = 0.0

        self.frame = 0 # 그냥 프레임 (열 프레임)

        self.row_frame = 0 # 행 프레임

        self.hp = 10

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
        self.Idle = []

        self.Create = {}

        self.intro_ground_dict = {}

        self.attack_dict = {}

        self.die_dict = {}

        self.in_put_resources()

        self.now_state_dict = self.Create

    pass


    def in_put_resources(self):
        # 리소스 기본상태
        path = 'BossPotato/PotatoResource/BossPotato.png'  # main.py 기준임
        if Boss_Potato.Boss_image is None:
            Boss_Potato.Boss_image = load_image(path)
        self.image = Boss_Potato.Boss_image
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?

        # 여기에 이미지 관련 정보 set 함수 적기

        # 보스 intro 모션
        self.set_in_game_motion()
        self.set_intro_ground_motion()
        self.set_attack_motion()
        self.set_die_motion()

        # 보스 일반 공격 모션




    def set_in_game_motion(self):
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?
        # self.Idle = [526,512,20,7,4522,8,6]
        self.Create['width'] = 526  # 가로크기
        self.Create['high'] = 511  # 세로크기
        self.Create['frame'] = 20  # 총 몇 프레임인지?
        self.Create['frame_speed'] = 20  # 프레임 속도
        self.Create['column_frame'] = 6  # 가로 프레임 몇 개인지?
        self.Create['row_frame'] = 4  # 세로 프레임 몇 개인지?
        self.Create['last_row_frame'] = 2  # 마지막 줄 가로 프레임
        self.Create['left'] = 7  # x값 어디서부터 시작하는지?
        self.Create['bottom'] = 4522  # y값 어디서부터 시작하는지?
        self.Create['go_right'] = 531  # x값 얼마만큼 떨어지는지?
        self.Create['go_down'] = 517  # y값 얼마만큼 떨어지는지?
        pass

    def set_intro_ground_motion(self):
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?
        # self.Idle = [526,512,20,7,4522,8,6]
        self.intro_ground_dict['width'] = 557  # 가로크기
        self.intro_ground_dict['high'] = 460  # 세로크기
        self.intro_ground_dict['frame'] = 19  # 총 몇 프레임인지?
        self.intro_ground_dict['frame_speed'] = 20  # 프레임 속도
        self.intro_ground_dict['column_frame'] = 5  # 가로 프레임 몇 개인지?
        self.intro_ground_dict['row_frame'] = 4  # 세로 프레임 몇 개인지?
        self.intro_ground_dict['last_row_frame'] = 4  # 마지막 줄 가로 프레임
        self.intro_ground_dict['left'] = 2  # x값 어디서부터 시작하는지?
        self.intro_ground_dict['bottom'] = 6487  # y값 어디서부터 시작하는지?
        self.intro_ground_dict['go_right'] = 558  # x값 얼마만큼 떨어지는지?
        self.intro_ground_dict['go_down'] = 462  # y값 얼마만큼 떨어지는지?
        pass

    def set_attack_motion(self):
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?
        # self.Idle = [526,512,20,7,4522,8,6]
        self.attack_dict['width'] = 526  # 가로크기
        self.attack_dict['high'] = 511  # 세로크기
        self.attack_dict['frame'] = 17  # 총 몇 프레임인지? 1 부터 시작
        self.attack_dict['frame_speed'] = 20  # 프레임 속도
        self.attack_dict['column_frame'] = 6  # 가로 프레임 몇 개인지?
        self.attack_dict['row_frame'] = 3  # 세로 프레임 몇 개인지?
        self.attack_dict['last_row_frame'] = 5  # 마지막 줄 가로 프레임
        self.attack_dict['left'] = 7  # x값 어디서부터 시작하는지?
        self.attack_dict['bottom'] = 2391  # y값 어디서부터 시작하는지?
        self.attack_dict['go_right'] = 531  # x값 얼마만큼 떨어지는지?
        self.attack_dict['go_down'] = 517  # y값 얼마만큼 떨어지는지?
        pass

    def set_die_motion(self):
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?
        # self.Idle = [526,512,20,7,4522,8,6]
        self.die_dict['width'] = 303  # 가로크기
        self.die_dict['high'] = 439  # 세로크기
        self.die_dict['frame'] = 9  # 총 몇 프레임인지?
        self.die_dict['frame_speed'] = 20  # 프레임 속도
        self.die_dict['column_frame'] = 9  # 가로 프레임 몇 개인지?
        self.die_dict['row_frame'] = 1  # 세로 프레임 몇 개인지?
        self.die_dict['last_row_frame'] = 9  # 마지막 줄 가로 프레임
        self.die_dict['left'] = 7  # x값 어디서부터 시작하는지?
        self.die_dict['bottom'] = 850  # y값 어디서부터 시작하는지?
        self.die_dict['go_right'] = 308  # x값 얼마만큼 떨어지는지?
        self.die_dict['go_down'] = 439  # y값 얼마만큼 떨어지는지?
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
        #World_collision.player_skill_collision()
        pass

    def render(self):

        if self.intro_ground_frame < 8 and self.now_state_dict == self.Create:
            # 이건 인트로 때만 동작
            if self.now_state_dict == self.Create:
                self.image.clip_composite_draw(int(self.intro_ground_dict['left'] + (
                        self.intro_ground_dict['go_right'] * int(
                    int(self.intro_ground_frame) % self.intro_ground_dict['column_frame']))),
                                               int(self.intro_ground_dict['bottom'] - (
                                                       self.intro_ground_dict[
                                                           'go_down'] * self.intro_ground_row_frame)),
                                               self.intro_ground_dict['width'],
                                               self.intro_ground_dict['high'], 0, '', self.CX + 20, self.CY - 50,
                                               self.intro_ground_dict['width'] * self.boss_size,
                                               self.intro_ground_dict['high'] * self.boss_size)
            return


        self.image.clip_composite_draw(int(self.now_state_dict['left'] + (self.now_state_dict['go_right'] * int(int(self.frame) % self.now_state_dict['column_frame']))),
                                       int(self.now_state_dict['bottom'] - (self.now_state_dict['go_down'] * self.row_frame)),
                                       self.now_state_dict['width'],
                                       self.now_state_dict['high'],0,'',self.CX,self.CY,
                                       self.now_state_dict['width'] * self.boss_size,self.now_state_dict['high'] * self.boss_size)

        if self.intro_ground_frame <= 18:
            # 이건 인트로 때만 동작
            if self.now_state_dict == self.Create:
                self.image.clip_composite_draw(int(self.intro_ground_dict['left'] + (
                        self.intro_ground_dict['go_right'] * int(
                    int(self.intro_ground_frame) % self.intro_ground_dict['column_frame']))),
                                               int(self.intro_ground_dict['bottom'] - (
                                                       self.intro_ground_dict['go_down'] * self.intro_ground_row_frame)),
                                               self.intro_ground_dict['width'],
                                               self.intro_ground_dict['high'], 0, '', self.CX, self.CY - 50,
                                               self.intro_ground_dict['width'] * self.boss_size,
                                               self.intro_ground_dict['high'] * self.boss_size)

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


        if self.now_state_dict == self.Create:
            self.intro_ground_frame += 1 * self.intro_ground_dict['frame_speed'] * frametime.frame_time
            self.intro_ground_row_frame = int(self.intro_ground_frame / self.intro_ground_dict['column_frame'])
            if self.frame >= self.now_state_dict['frame']:
                self.frame = 0
                self.row_frame = 0


        if self.before_state_dict == self.now_state_dict:
            self.frame += 1 * self.now_state_dict['frame_speed'] * frametime.frame_time
            self.row_frame = int(self.frame / self.now_state_dict['column_frame'])

            # 이건 인트로 때만 동작
            if self.now_state_dict == self.Create:
                if self.intro_ground_frame < 8:
                    self.frame = 0
                    self.row_frame = 0


            if self.frame >= self.now_state_dict['frame']:

                # 여기서 처음모션에서 아이들 모션으로 바꾸어 줌 # 인트로 때만 동작
                if self.now_state_dict == self.Create:
                    self.now_state_dict = self.attack_dict # 일단은 반복

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
        rand_num = random.randint(0,10)
        if rand_num >= 7:
            bullet = Boss_potato_skill_item()
            bullet.CX = self.CX - self.boss_potato_rx
            bullet.CY = self.CY - self.boss_potato_ry * 0.7
            object_manager.input_object(bullet, object_manager.player_skill_item_num)
        else:
            bullet = Boss_potato_skill()
            bullet.CX = self.CX - self.boss_potato_rx
            bullet.CY = self.CY - self.boss_potato_ry * 0.7
            object_manager.input_object(bullet,object_manager.boss_skill_list_num)
        pass