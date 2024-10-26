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

        self.gravity = True # 중력을 현재 적용 하는지?

        self.gravity_time = 0.0 # 중력 시간 값

        self.gravity_speed = 3.5 # 중력 값

        self.CX = 100

        self.CY = 300

        self.frame = 0

        self.LR = False # True 이면 왼쪽 False 이면 오른쪽

        self.hit_bool = False # 맞은 상태인지?

        self.in_put_resources()

    # 움직임 관련 변수
        # 달리기
        self.running = False
        self.rundir = 0
        self.run_speed = 10
        # 점프
        self.jump_high = 25
        self.jump_angle = 0
        self.jumping = False

        # 기본 공격
        self.normal_attaking = False
        self.normal_attaking_angle = 0
        self.normal_attaking_high = 10

        # 각 상태에 대한 구조체 정의 [프레임 개수, 프레임 속도, 이미지 배열]
        self.idle = [8,0.2,self.image_Idle]
        self.hit = [6,0.2,self.image_Hit]
        self.jump = [8,0.4,self.image_Jump]
        self.nomal_attak = [8,0.4,self.image_Nomal_Attak]
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


    def player_state_updete(self): # 플레이어 상태가 변경 될 때 해주어야 할 것들

        frame = 0

        pass


    def player_left_right_key_down(self,key):

        if key == SDLK_RIGHT:
            self.LR = False

        elif key == SDLK_LEFT:
            self.LR = True

        elif key == SDLK_SPACE:
            if self.jumping:
                self.normal_attaking = True

            self.jumping = True

        pass

    def player_left_right_key_up(self, key):



        pass

    # 움직임 관련 함수
    def player_move_run(self):
        if self.rundir < 0:
            self.running = True
            self.CX -= self.run_speed
            self.now_state_tuple = self.run

        elif self.rundir > 0:
            self.running = True
            self.CX += self.run_speed
            self.now_state_tuple = self.run
        else:
            self.running = False
            self.now_state_tuple = self.idle

        pass


    def player_move_jump(self):
        if self.jumping:
            if self.normal_attaking == True:
                self.jump_angle = 0
                self.CY += math.sin(math.radians(self.normal_attaking_angle)) * self.normal_attaking_high - 9.8 * (
                            self.normal_attaking_angle / 180)
                self.now_state_tuple = self.nomal_attak
                if self.normal_attaking_angle < 350:
                    self.normal_attaking_angle += 7  # 사실상 점프 속도
                else:
                    self.normal_attaking_angle = 0
                pass
            else:
                self.normal_attaking_angle = 0
                if self.jumping:
                    self.CY += math.sin(math.radians(self.jump_angle)) * self.jump_high - 9.8 * (self.jump_angle / 180)
                    self.now_state_tuple = self.jump
                    if self.jump_angle < 350:
                        self.jump_angle += 7  # 사실상 점프 속도
                else:
                    self.jump_angle = 0
                    self.normal_attaking_angle = 0
            pass

    def player_move_skill(self):

        pass


    def player_move_hit(self):
        if self.hit_bool:
            self.now_state_tuple = self.hit
        pass

    def player_move_clear(self):

        pass

    def player_move(self):
        self.player_move_run()
        self.player_move_jump()
        self.player_move_hit()
        self.player_gravity()
        pass


    def player_resource_state(self):
        pass



    def player_gravity(self):

        if self.gravity:
            self.gravity_time += 0.1
            self.CY -= self.gravity_speed * self.gravity_time
        else:
            self.gravity_time = 0.0

        pass




    def key_input_down(self, key):
        self.player_left_right_key_down(key)
        if key == SDLK_RIGHT:

            self.rundir += 1
            self.player_state_updete()
            pass

        elif key == SDLK_SPACE:
            self.now_state_tuple = self.jump
            self.player_state_updete()
            pass


        elif key == SDLK_LEFT:

            self.rundir -= 1
            self.player_state_updete()
            pass

        elif key == SDLK_t:
            self.CY = 400
            self.gravity = True

            pass
        elif key == SDLK_k:
            self.hit_bool = True
            self.player_state_updete()

        else:
            self.now_state_tuple = self.idle
            self.player_state_updete()
            pass


        pass

    def key_input_up(self, key):
        self.player_left_right_key_up(key)
        if key == SDLK_RIGHT:
            self.rundir -= 1
            pass

        elif key == SDLK_SPACE:

            pass

        elif key == SDLK_LEFT:
            self.rundir += 1

            pass
        else:
            self.now_state_tuple = self.idle
            self.player_state_updete()
            pass

        pass

    def update_change_state(self):
        if self.now_state_tuple == self.hit:
            self.hit_bool = False  # 맞은 상태 끝!
            self.player_state_updete()
        pass


    def update(self):

        self.player_move()


        self.frame += 1 * self.now_state_tuple[1]
        if self.frame >= self.now_state_tuple[0]:

            self.update_change_state()

            self.frame = 0

        pass



    def late_update(self):
        pass

    def render(self):
        if self.LR == True:
            self.now_state_tuple[2][int(self.frame)].clip_composite_draw(0,0,300,300,0,'h',self.CX,self.CY)
        else:
            self.now_state_tuple[2][int(self.frame)].draw(self.CX,self.CY)
        pass
