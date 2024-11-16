import math

from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime



class Player_skill_cup:
    image_attack = None
    def __init__(self):

        self.this_delete = False  # 이 객체를 지워야 하는지?

        self.move_speed = 50.0

        self.CX = 100

        self.CY = 300

        self.skill_size = 0.8

        self.LR = True # True면 오른쪽


        self.frame = 0.0


        self.in_put_resources()



        self.state_attack = [41,20.0,self.image_attack]



        self.now_state_tuple = self.state_attack


        pass


    def in_put_resources(self):
        # 리소스 기본상태
        if Player_skill_cup.image_attack == None:
            path = 'CupHeadBanging/PlayerResoures/Skill1_ShootCup/player_skill_cup'  # main.py 기준임
            Player_skill_cup.image_attack = []
            for a in range(0, 40+1):
                finalPath = path + str(a) + '.png'
                Player_skill_cup.image_attack.append(load_image(finalPath))


    def player_skill_cup_move(self):
        if self.LR == True: # 오른쪽
            self.CX += self.move_speed * frametime.frame_time
        else:
            self.CX -= self.move_speed * frametime.frame_time
        pass

    def skill_update(self):
        if self.now_state_tuple == self.state_attack:
            self.this_delete = True
        pass


    def player_skill_cup_resource_state(self):

        self.before_state_tuple = self.now_state_tuple

        if self.before_state_tuple == self.now_state_tuple:
            self.frame += 1.0 * self.now_state_tuple[1] * frametime.frame_time
            if self.frame >= self.now_state_tuple[0]:
                self.skill_update()
                self.frame = 0.0

        pass



    def key_input_down(self, key):


        pass

    def key_input_up(self, key):


        pass


    def update(self):

        self.player_skill_cup_resource_state()

        self.player_skill_cup_move()

        self.player_skill_cup_rx =  self.now_state_tuple[2][int(self.frame)].w * 0.5
        self.player_skill_cup_ry = self.now_state_tuple[2][int(self.frame)].h * 0.5

        pass



    def late_update(self):


          pass

    def render(self):
        if self.LR == False:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0,0,700,700,0,'h',self.CX,self.CY,
                                        self.now_state_tuple[2][int(self.frame)].w * self.skill_size,self.now_state_tuple[2][int(self.frame)].h * self.skill_size)
        else:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0,0,700,700,0,'',self.CX,self.CY,
                                        self.now_state_tuple[2][int(self.frame)].w * self.skill_size,self.now_state_tuple[2][int(self.frame)].h * self.skill_size)

        pico2d.draw_rectangle(self.get_collision_size()[0],self.get_collision_size()[1],
                              self.get_collision_size()[2],self.get_collision_size()[3])

        pass

    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX - self.player_skill_cup_rx, self.CY + self.player_skill_cup_ry, self.CX + self.player_skill_cup_rx, self.CY - self.player_skill_cup_ry