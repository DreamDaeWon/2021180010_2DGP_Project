from math import radians

from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime
import object_manager


class Boss_Blue_Player_Item:
    image = None
    def __init__(self, angle, dir):

        self.this_delete = False # 이 객체를 지워야 하는지?

        self.angle = angle

        self.dir = dir

        self.CX = 0
        self.CY = object_manager.world[object_manager.boss_list_num][0].CY + object_manager.world[object_manager.boss_list_num][0].boss_blue_ry * 2

        self.moveX = 0

        self.RealCX = object_manager.world[object_manager.boss_list_num][0].RealCX - object_manager.world[object_manager.boss_list_num][0].boss_blue_rx



        self.rx = 0.0
        self.ry = 0.0

        self.move_speed = 50.0

        self.frame = 0.0

        self.now_state_tuple = 0

        self.image_question = 0

        self.want_move_vec_X = 0
        self.want_move_vec_Y = 1

        self.in_put_resources()

        # 각 상태에 대한 구조체 정의 [프레임 개수, 프레임 속도, 이미지 배열]
        self.attack_tuple = [7,15,self.image_question]

        self.now_state_tuple = self.attack_tuple

        self.before_state_tuple = 0

        self.size = 0.7

        self.rotate_point(self.want_move_vec_X,self.want_move_vec_Y,self.angle)



        pass

    def rotate_point(self, x, y, angle_degrees):
        # 각도를 라디안으로 변환
        angle_radians = math.radians(angle_degrees)
        # 회전 변환 공식 적용
        self.want_move_vec_X = x * math.cos(angle_radians) - y * math.sin(angle_radians)
        self.want_move_vec_X = x * math.sin(angle_radians) + y * math.cos(angle_radians)
        return

    def in_put_resources(self):
        self.set_player_item_image()
        pass

    def set_player_item_image(self):
        if Boss_Blue_Player_Item.image is None:
            Boss_Blue_Player_Item.image = []

            path = 'Resources/Blue_Boss/Phase 1/Transition To Ph2/Question Marks/c_slime_question_mark_000'  # main.py 기준임

            for a in range(1, 7 + 1):
                finalPath = path + str(a) + '.png'
                Boss_Blue_Player_Item.image.append(load_image(finalPath))

        self.image_question = []
        self.image_question = Boss_Blue_Player_Item.image
        pass


    def boss_skill_state_update(self):

        pass

    def boss_skill_resource_state(self):
        self.before_state_tuple = self.now_state_tuple


        if self.before_state_tuple == self.now_state_tuple:
            self.frame += 1 * self.now_state_tuple[1] * frametime.frame_time


            if self.frame >= self.now_state_tuple[0]:
                self.frame = 0
        else:
            self.boss_skill_state_update()
            print('in this')
        pass

    def update(self):

        self.moveX = object_manager.world[object_manager.back_ground_list_num][0].moveX



        self.boss_skill_resource_state()

        self.boss_skill_move()
        self.CX = self.RealCX + self.moveX


        self.rx = self.now_state_tuple[2][int(self.frame)].w * 0.5 * self.size
        self.ry = self.now_state_tuple[2][int(self.frame)].h * 0.5 * self.size


        pass

    def late_update(self):

        pass

    def render(self):

        self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0, 0, self.now_state_tuple[2][int(self.frame)].w,
                                                                     self.now_state_tuple[2][int(self.frame)].h,
                                                                     radians(self.angle),
                                                                     '',
                                                                     self.CX - self.rx,
                                                                     self.CY - self.ry,
                                                                     self.rx * 2,
                                                                     self.ry * 2
                                                                     )

        #pico2d.draw_rectangle(self.get_collision_size()[0],self.get_collision_size()[1],self.get_collision_size()[2],self.get_collision_size()[3])
        pass

    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass

    def boss_skill_move(self):
        self.RealCX += self.move_speed * self.want_move_vec_X * frametime.frame_time * self.dir
        self.CY += self.move_speed * self.want_move_vec_Y * frametime.frame_time
        pass

    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX - self.rx * 2, self.CY, self.CX, self.CY - self.ry * 2