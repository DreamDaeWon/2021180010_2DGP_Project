import enum

import math

from pico2d import *


import stage_manager


import Game.CupHeadBanging.player_skill_cup

from Game.BossPotato.boss_potato import Boss_Potato

from Game.UI.ui_black_circle import Ui_Black_Circle

from Game.collision import World_collision

import os
import sys



# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir)  # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir)  # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime
import object_manager


class PlayerState(enum.Enum):
    IDLE = 0
    MOVE_RIGHT = 1
    MOVE_LEFT = 2
    HIT = 3
    JUMP = 4


class CupheadBanging:
    def __init__(self, now_stage):

        self.now_stage = now_stage

        self.this_delete = False  # 이 객체를 지워야 하는지?

        self.PlayerState = PlayerState.IDLE  # Player State

        self.Right = True  # 플레이어 방향 오른쪽인지?

        self.gravity = True  # 중력을 현재 적용 하는지?

        self.LR = False

        self.gravity_time = 0.0  # 중력 시간 값

        self.gravity_speed = 5.5  # 중력 값

        self.CX = 100

        self.CY = 300

        self.Player_Size = 0.8

        self.player_rx = 0.0

        self.player_ry = 0.0

        self.frame = 0.0

        self.skill_number = 0  # 스킬 개수

        # 왼쪽 오른쪽 키 입력
        self.Left_Key_Down = False
        self.Right_Key_Down = False

        self.key_input_LR = False  # 현재 키가 눌려있는 상태인지?

        self.hit_bool = False  # 맞은 상태인지?

        self.in_put_resources()

        # 움직임 관련 변수
        # 달리기
        self.running = False
        self.rundir = 0
        self.run_speed = 700
        # 점프
        self.jump_high = 6
        self.jump_angle = 0
        self.jumping = False

        # 기본 공격
        self.normal_attaking = False
        self.normal_attaking_angle = 0
        self.normal_attaking_high = 3

        # 스킬사용
        self.stop = False
        self.skill_freeze_time = 0.0 # 2초동안 가만히

        # 체력
        self.hp = 5


        # 각 상태에 대한 구조체 정의 [프레임 개수, 프레임 속도, 이미지 배열]
        self.idle = [8, 15, self.image_Idle]
        self.hit = [6, 13, self.image_Hit]
        self.jump = [8, 17, self.image_Jump]
        self.normal_attak = [8, 17, self.image_Nomal_Attak]
        self.clear = [36, 16, self.image_Clear]
        self.run = [16, 25, self.image_Run]
        self.die = [24,25,self.image_Die]

        # 현재 상태 배열
        self.now_state_tuple = self.idle
        self.before_state_tuple = self.idle

    def in_put_resources(self):
        # 리소스 기본상태
        path = 'CupHeadBanging/PlayerResoures/Idle/cuphead_idle_000'  # main.py 기준임
        self.image_Idle = []
        for a in range(1, 8 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Idle.append(load_image(finalPath))

        # 리소스 맞는상태
        path = 'CupHeadBanging/PlayerResoures/Hit/cuphead_hit_air_000'  # main.py 기준임
        self.image_Hit = []
        for a in range(1, 6 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Hit.append(load_image(finalPath))

        # 리소스 점프상태
        path = 'CupHeadBanging/PlayerResoures/Jump/cuphead_jump_000'  # main.py 기준임
        self.image_Jump = []
        for a in range(1, 8 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Jump.append(load_image(finalPath))

        # 리소스 점프공격 상태
        path = 'CupHeadBanging/PlayerResoures/Attak/Hand/cuphead_parry_000'  # main.py 기준임
        self.image_Nomal_Attak = []
        for a in range(1, 8 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Nomal_Attak.append(load_image(finalPath))

        # 리소스 클리어 상태
        path = 'CupHeadBanging/PlayerResoures/Clear/player_ch_powerup_'  # main.py 기준임
        self.image_Clear = []
        for a in range(1, 36 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Clear.append(load_image(finalPath))

        # 리소스 달리기 상태
        path = 'CupHeadBanging/PlayerResoures/Run/cuphead_run_'  # main.py 기준임
        self.image_Run = []
        for a in range(1, 16 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Run.append(load_image(finalPath))

            # 리소스 죽음 상태
        path = 'CupHeadBanging/PlayerResoures/Die/cuphead_ghost_'  # main.py 기준임
        self.image_Die = []
        for a in range(1, 24 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Die.append(load_image(finalPath))


    def player_state_updete(self):  # 플레이어 상태가 변경 될 때 해주어야 할 것들

        #if self.hit_bool:
        if self.before_state_tuple != self.now_state_tuple:
            self.frame = 0.0
            #self.now_state_tuple = self.idle
            #return

        #s elf.frame = 0

        pass

    def player_left_right_key_down(self, key):

        if self.now_state_tuple == self.die:
            return

        if self.stop:
            return

        if key == SDLK_RIGHT:
            self.LR = False

        elif key == SDLK_LEFT:
            self.LR = True

        pass

    def player_left_right_key_up(self, key):

        pass

    # 움직임 관련 함수
    def player_move_run(self):
        if self.Left_Key_Down == True and self.Right_Key_Down == False:
            self.running = True
            self.CX -= self.run_speed * frametime.frame_time
            #self.now_state_tuple = self.run

        elif self.Left_Key_Down == False and self.Right_Key_Down == True:
            self.running = True
            self.CX += self.run_speed * frametime.frame_time
            #self.now_state_tuple = self.run
        else:
            self.running = False
            #self.now_state_tuple = self.idle

        pass

    def player_move_jump(self):
        if self.jumping:
            if self.normal_attaking == True:
                self.jump_angle = 0
                self.CY += math.sin(math.radians(self.normal_attaking_angle)) * self.normal_attaking_high - 5.8 * (
                        self.normal_attaking_angle / 180)
                self.now_state_tuple = self.normal_attak
                if self.normal_attaking_angle < 350:
                    self.normal_attaking_angle += frametime.frame_time * 300  # 사실상 점프 속도
                else:
                    self.normal_attaking_angle = 0
                pass
            else:
                self.normal_attaking_angle = 0
                if self.jumping:
                    self.CY += math.sin(math.radians(self.jump_angle)) * self.jump_high - 5.8 * (self.jump_angle / 180)
                    self.now_state_tuple = self.jump
                    if self.jump_angle < 350:
                        self.jump_angle += frametime.frame_time * 300  # 사실상 점프 속도
                else:
                    self.jump_angle = 0
                    self.normal_attaking_angle = 0
            pass

    def player_move_skill(self):

        pass

    def player_move_hit(self):
        if self.hit_bool:
            #if self.gravity == False and self.gravity_time != 0.0:
            self.now_state_tuple = self.hit
            self.CY += math.sin(math.radians(self.jump_angle)) * self.jump_high - 5.8 * (self.jump_angle / 180)
            if self.jump_angle < 350:
                self.jump_angle += frametime.frame_time * 300  # 사실상 점프 속도
        pass

    def player_move_clear(self):

        pass

    def player_move(self):

        if self.now_state_tuple == self.die:
            self.player_gravity()
            return

        if self.stop:
            return

        if self.now_state_tuple != self.hit:
            self.player_move_run()
            self.player_move_jump()
            self.player_gravity()

        self.player_move_hit()

        pass

    def player_resource_state(self):



        self.before_state_tuple = self.now_state_tuple



        self.now_state_tuple = self.idle

        if self.running:
            self.now_state_tuple = self.run

        if self.jumping:
            self.now_state_tuple = self.jump

        if self.normal_attaking:
            self.now_state_tuple = self.normal_attak

        if self.hit_bool:
            self.now_state_tuple = self.hit


        # 죽었다면?
        if self.hp <= 0:
            self.now_state_tuple = self.die

        if self.frame >= self.now_state_tuple[0]:
            self.frame = 0.0
            pass

        if self.before_state_tuple == self.now_state_tuple:
            self.frame += 1.0 * self.now_state_tuple[1] * frametime.frame_time
            if self.frame >= self.now_state_tuple[0]:
                self.update_change_state()
                self.frame = 0.0
        else:
            self.player_state_updete()
            #print('in this')

        pass

    def player_gravity(self):

        if self.gravity:
            self.gravity_time += frametime.frame_time
            self.CY -= self.gravity_speed * self.gravity_time
        else:
            self.gravity_time = 0.0

        pass

    def key_input_down(self, key):

        #if self.hit_bool:
        #    self.rundir = 0
        #    return

        if self.hp == 0:
            return

        self.player_left_right_key_down(key)

        if key == SDLK_RIGHT:

            self.Right_Key_Down = True
            self.player_state_updete()
            pass

        elif key == SDLK_LEFT:

            self.Left_Key_Down = True
            self.player_state_updete()
            pass

        elif key == SDLK_z:
            if self.skill_number > 0:
                self.skill_number -= 1
                self.shoot_skill()


        elif key == SDLK_SPACE:

            if self.jumping:
                self.normal_attaking = True

            self.jumping = True

        elif key == SDLK_t:
            self.CY = 400
            self.gravity = True



            pass
        elif key == SDLK_k:
            self.hit_bool = True
            self.player_state_updete()

        elif key == SDLK_b:
            object_manager.world[1].append(Boss_Potato())
            World_collision.get_boss(object_manager.world[1][0])

        else:
            #self.now_state_tuple = self.idle
            #self.player_state_updete()
            pass

        pass

    def key_input_up(self, key):

        self.player_left_right_key_up(key)
        if key == SDLK_RIGHT:
            self.Right_Key_Down = False
            self.rundir -= 1
            pass

        elif key == SDLK_LEFT:
            self.Left_Key_Down = False
            self.rundir += 1

            pass

        pass

    def update_change_state(self):
        if self.now_state_tuple == self.hit:
            self.hit_bool = False  # 맞은 상태 끝!
            #self.rundir = 0
            if self.hp > 0:
                self.hp -= 1
                if self.hp == 0:
                    object_manager.delete_want_list(object_manager.UI_list_num)
                    object_manager.world[object_manager.UI_list_num].append(Ui_Black_Circle(self.now_stage))


            self.gravity = True
            self.gravity_time = 0.0
            self.jump_angle = 0
            self.now_state_tuple = self.idle
        pass

    def update(self):

        self.check_stop_time()

        self.player_resource_state()

        self.player_move()

        self.player_rx = self.now_state_tuple[2][int(self.frame)].w * 0.5
        self.player_ry = self.now_state_tuple[2][int(self.frame)].h * 0.5

        pass

    def late_update(self):
        World_collision.player_collision()
        World_collision.boss_bullet_collision()
        World_collision.boss_bullet_item_collision()
        pass

    def render(self):
        if self.LR == True:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0, 0, 300, 300, 0, 'h', self.CX, self.CY,
                                                                         self.now_state_tuple[2][
                                                                             int(self.frame)].w * self.Player_Size,
                                                                         self.now_state_tuple[2][
                                                                             int(self.frame)].h * self.Player_Size)
        else:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0, 0, 300, 300, 0, '', self.CX, self.CY,
                                                                         self.now_state_tuple[2][
                                                                             int(self.frame)].w * self.Player_Size,
                                                                         self.now_state_tuple[2][
                                                                             int(self.frame)].h * self.Player_Size)

        pico2d.draw_rectangle(self.get_collision_size()[0], self.get_collision_size()[1],
                              self.get_collision_size()[2], self.get_collision_size()[3])

        pass

    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX - self.player_rx, self.CY + self.player_ry, self.CX + self.player_rx, self.CY - self.player_ry

    def shoot_skill(self):
        bullet = Game.CupHeadBanging.player_skill_cup.Player_skill_cup()
        bullet.CX = self.CX
        bullet.CY = self.CY
        bullet.LR = not self.LR
        object_manager.input_object(bullet, object_manager.player_skill_list_num)

        self.stop = True

        pass

    def check_stop_time(self):
        if self.stop:
            if self.skill_freeze_time < 1.0:
                self.skill_freeze_time += frametime.frame_time

            else:
                self.skill_freeze_time = 0.0
                self.stop = False
        pass
