import enum

import math

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

        self.CX = 100

        self.CY = 100

        self.frame = 0

        self.LR = 0 # -1 이면 왼쪽 1 이면 오른쪽

        self.in_put_resources()

    # 움직임 관련 변수
        # 달리기
        self.running = False
        self.rundir = 0
        self.run_speed = 5
        # 점프
        self.jump_high = 150
        self.jump_angle = 0
        self.jumping = False


        # 각 상태에 대한 구조체 정의 [프레임 개수, 프레임 속도, 이미지 배열]
        self.idle = [8,0.2,self.image_Idle]
        self.hit = [6,0.2,self.image_Hit]
        self.jump = [8,0.5,self.image_Jump]
        self.clear = [36,0.3,self.image_Clear]
        self.run = [16,0.4,self.image_Run]

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

        # 리소스 달리기 상태
        path = 'CupHeadBanging/PlayerResoures/Run/cuphead_run_'  # main.py 기준임
        self.image_Run = []
        for a in range(1, 16 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Run.append(load_image(finalPath))


    def player_state_updete(self): # 플레이어 상태가 변경 될 때 해주어야 할 것들

        frame = 0

        pass


    def player_left_right_key_down(self,key):

        if key == SDLK_RIGHT:
            self.LR += 1

        elif key == SDLK_LEFT:
                self.LR -= 1

        pass

    def player_left_right_key_up(self, key):

        if key == SDLK_RIGHT:
            self.LR += 1

        elif key == SDLK_LEFT:
            self.LR -= 1

        pass

    # 움직임 관련 함수
    def player_move_run(self, key):
        if self.rundir < 0:
            self.running = True
            self.CX -= self.run_speed

        elif self.rundir > 0:
            self.running = True
            self.CX += self.run_speed
        else:
            self.running = False

        pass


    def player_move_jump(self):
        if self.jumping and self.jump_angle:
            self.CY += math.sin(math.radians(self.jump_angle)) * self.jump_high
        pass

    def player_move_skill(self):

        pass


    def player_move_hit(self):

        pass

    def player_move_clear(self):

        pass

    def player_move(self):

        pass



    def key_input_down(self, key):
        self.player_left_right_key_up(key)
        if key == SDLK_RIGHT:
            self.rundir = +1
            self.player_state_updete()
            pass
        elif key == SDLK_SPACE:
            self.now_state_tuple = self.jump
            self.player_state_updete()
            pass

        elif key == SDLK_LEFT:
            self.rundir = -1
            self.player_state_updete()
            pass
        else:
            self.now_state_tuple = self.idle
            self.player_state_updete()
            pass


        pass

    def key_input_up(self, key):
        self.player_left_right_key_up(key)
        if key == SDLK_RIGHT:
            self.rundir = -1
            pass

        elif key == SDLK_SPACE:

            pass

        elif key == SDLK_LEFT:
            self.rundir = +1

            pass
        else:
            self.now_state_tuple = self.idle
            self.player_state_updete()
            pass

        pass

    def update(self):

        self.player_move()

        self.frame += 1 * self.now_state_tuple[1]
        if self.frame >= self.now_state_tuple[0]:
            self.frame = 0

        pass

    def late_update(self):

        pass

    def render(self):
        if self.LR < 0:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0,0,300,300,0,'h',self.CX,self.CY)
        else:
            self.now_state_tuple[2][int(self.frame)].draw(self.CX,self.CY)
        pass
