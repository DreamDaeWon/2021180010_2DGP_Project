import enum
from unittest.mock import right

from pico2d import*

class PlayerState(enum.Enum):
    IDLE = 0
    MOVE_RIGHT = 1
    MOVE_LEFT = 2
    HIT = 3
    JUMP = 4




class CupheadBainging:
    def __init__(self):
        self.PlayerState = PlayerState.IDLE # Player State

        self.Right = True # 플레이어 방향 오른쪽인지?

        self.frame = 0

        self.LR = 0 # -1 이면 왼쪽 1 이면 오른쪽

        self.in_put_resources()

        # 각 상태에 대한 구조체 정의 [프레임 개수, 프레임 속도, 이미지 배열]
        self.idle = [8,0.2,self.image_Idle]
        self.hit = [6,0.2,self.image_Hit]
        self.jump = [8,0.5,self.image_Jump,150]
        self.clear = [36,0.3,self.image_Clear]

        # 현재 상태 배열
        self.now_state_tuple = self.idle

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

        # 리소스 클리어 상태
        path = 'CupHeadBanging/PlayerResoures/Clear/player_ch_powerup_'  # main.py 기준임
        self.image_Clear = []
        for a in range(1, 36 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Clear.append(load_image(finalPath))

    def player_state_updete(self): # 플레이어 상태가 변경 될 때 해주어야 할 것들

        frame = 0

        pass


    def player_left_right(self,key):



        pass

    def player_move_rum(self, key):

        pass


    def player_move_jump(self):

        pass

    def player_move_skill(self):

        pass

    def player_move_clear(self):

        pass

    def player_move(self):

        pass



    def key_input(self, key):
        if key == SDLK_RIGHT:
            self.Right += 1
            self.now_state_tuple = self.hit
            self.player_state_updete()
            pass
        #elif key == SDLK_LEFT:
        #    self.Right -= 1
        #    self.now_state_tuple = self.hit
        #    frame = 0
        #    pass
        elif key == SDLK_SPACE:
            self.now_state_tuple = self.jump
            self.player_state_updete()
            pass

        elif key == SDLK_LEFT:
            self.now_state_tuple = self.clear
            self.player_state_updete()
            pass
        else:
            self.now_state_tuple = self.idle
            self.player_state_updete()
            pass


        pass


    def update(self):

        self.frame += 1 * self.now_state_tuple[1]
        if self.frame >= self.now_state_tuple[0]:
            self.frame = 0

        self.player_move()

        pass

    def late_update(self):

        pass

    def render(self):

        self.now_state_tuple[2][int(self.frame)].draw(100,100)

        pass
