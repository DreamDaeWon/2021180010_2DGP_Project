import enum

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
        # 리소스 기본상태
        path = 'CupHeadBanging/PlayerResoures/Idle/cuphead_idle_000' # main.py 기준임
        self.image_Idle = []
        for a in range(1,5+1):
            finalPath = path + str(a) + '.png'
            self.image_Idle.append(load_image(finalPath))

        # 리소스 맞는상태
        path = 'CupHeadBanging/PlayerResoures/Hit/cuphead_hit_air_000'  # main.py 기준임
        self.image_Hit = []
        for a in range(1, 6+1):
            finalPath = path + str(a) + '.png'
            self.image_Hit.append(load_image(finalPath))

        # 리소스 맞는상태
        path = 'CupHeadBanging/PlayerResoures/Jump/cuphead_jump_000'  # main.py 기준임
        self.image_Jump = []
        for a in range(1, 8 + 1):
            finalPath = path + str(a) + '.png'
            self.image_Jump.append(load_image(finalPath))


        # 각 상태에 대한 구조체 정의 [프레임 개수, 프레임 속도, 이미지 배열]
        self.idle = [5,0.1,self.image_Idle]
        self.hit = [6,0.1,self.image_Hit]
        self.jump = [8,0.5,self.image_Jump]

        # 현재 상태 배열
        self.now_state_tuple = self.idle



    def key_input(self, key):
        if key == SDLK_RIGHT:
            self.Right += 1
            self.now_state_tuple = self.hit
            frame = 0
            pass
        elif key == SDLK_LEFT:
            self.Right -= 1
            self.now_state_tuple = self.hit
            frame = 0
            pass
        elif key == SDLK_SPACE:
            self.now_state_tuple = self.jump
            frame = 0
            pass
        else:
            self.now_state_tuple = self.idle
            frame = 0
            pass


        pass


    def update(self):

        self.frame += 1 * self.now_state_tuple[1]

        if self.frame >= self.now_state_tuple[0]:
            self.frame = 0

        pass

    def late_update(self):

        pass

    def render(self):
        self.now_state_tuple[2][int(self.frame)].draw(100,100)

        pass