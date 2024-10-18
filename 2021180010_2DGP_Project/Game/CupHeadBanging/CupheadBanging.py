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
            self.image_Hit.append(load_image(finalPath))


        self.idle_maxFrame = 5
        self.hit_maxFrame = 6

    def key_input(self, key):
        if key == SDLK_RIGHT:
            self.PlayerState = PlayerState.MOVE
            pass
        elif key == SDLK_SPACE:
            pass
        pass


    def update(self):
        self.frame += 1
        if self.frame >= self.hit_maxFrame:
            self.frame = 0

        pass

    def late_update(self):

        pass

    def render(self):
        self.image_Hit[self.frame].draw(100,100)
        pass