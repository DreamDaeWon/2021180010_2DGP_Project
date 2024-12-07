from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime


class Boss_potato_skill_item:
    image = None
    def __init__(self):

        self.this_delete = False # 이 객체를 지워야 하는지?

        self.CX = 0.0
        self.CY = 0.0

        self.rx = 0.0
        self.ry = 0.0

        self.move_speed = 500.0

        self.frame = 0.0

        self.now_state_dict = 0


        self.attack_dict = {}


        self.in_put_resources()

        self.now_state_dict = self.attack_dict

        self.size = 0.7


        pass


    def in_put_resources(self):
        # 리소스 기본상태
        path = 'Resources/PotatoResource/player_item.png'  # main.py 기준임
        if Boss_potato_skill_item.image is None:
            Boss_potato_skill_item.image = load_image(path)
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?

        # 여기에 이미지 관련 정보 set 함수 적기
        # 보스 intro 모션
        self.set_attack_motion()


        # 보스 일반 공격 모션

    def set_attack_motion(self):
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?
        # self.Idle = [526,512,20,7,4522,8,6]
        self.attack_dict['width'] = 132  # 가로크기
        self.attack_dict['high'] = 142  # 세로크기
        self.attack_dict['frame'] = 4  # 총 몇 프레임인지? 1 부터 시작
        self.attack_dict['frame_speed'] = 10  # 프레임 속도
        self.attack_dict['column_frame'] = 4  # 가로 프레임 몇 개인지?
        self.attack_dict['row_frame'] = 1  # 세로 프레임 몇 개인지?
        self.attack_dict['last_row_frame'] = 4  # 마지막 줄 가로 프레임
        self.attack_dict['left'] = 0  # x값 어디서부터 시작하는지?
        self.attack_dict['bottom'] = 0  # y값 어디서부터 시작하는지?
        self.attack_dict['go_right'] = 132  # x값 얼마만큼 떨어지는지?
        self.attack_dict['go_down'] = 142  # y값 얼마만큼 떨어지는지?
        pass

    def boss_skill_state_update(self):

        pass

    def boss_skill_resource_state(self):
        self.before_state_dict = self.now_state_dict


        if self.before_state_dict == self.now_state_dict:
            self.frame += 1 * self.now_state_dict['frame_speed'] * frametime.frame_time
            self.row_frame = int(self.frame / self.now_state_dict['column_frame'])


            if self.frame >= self.now_state_dict['frame']:
                self.frame = 0
                self.row_frame = 0
        else:
            self.boss_skill_state_update()
            print('in this')
        pass

    def update(self):

        self.boss_skill_resource_state()

        self.boss_skill_move()

        self.rx =  self.now_state_dict['width'] * 0.5 * self.size
        self.ry = self.now_state_dict['high'] * 0.5 * self.size


        pass

    def late_update(self):

        pass

    def render(self):

        self.image.clip_composite_draw(int(self.now_state_dict['left'] + (self.now_state_dict['go_right'] * int(int(self.frame) % self.now_state_dict['column_frame']))),
                                       int(self.now_state_dict['bottom'] - (self.now_state_dict['go_down'] * self.row_frame)),
                                       self.now_state_dict['width'],
                                       self.now_state_dict['high'],0,'',self.CX,self.CY,
                                       self.now_state_dict['width'] * self.size,self.now_state_dict['high'] * self.size)

        #pico2d.draw_rectangle(self.get_collision_size()[0],self.get_collision_size()[1],self.get_collision_size()[2],self.get_collision_size()[3])
        pass

    def key_input_down(self, Key):
        pass

    def key_input_up(self, Key):
        pass

    def boss_skill_move(self):
        self.CX -= self.move_speed * frametime.frame_time
        pass

    def get_collision_size(self):
        # left, top ,right, bottom
        return self.CX - self.rx, self.CY + self.ry, self.CX + self.rx, self.CY - self.ry