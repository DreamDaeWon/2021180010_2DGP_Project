from dw_define import*

class Collision:
    def __init__(self):
        self.all_object = 0 # 모든 객체를 받아올 것임

        self.player = 0 # 플레이어 객체를 받아올 것임

        self.player_bullet = 0 # 플레이어 총알 객체 리스트를 받아올 것임

        self.boss = 0 # 보스 객체를 받아 올 것임

        self.boss_bullet = 0 # 보스의 총알 객체 리스트를 받아올 것임

        self.ground = 0 # 땅 받아오기

        pass


    def get_player(self, player): # 플레이어 받아오기
        self.player = player
        pass

    def get_ground(self, ground):  # 땅 받아오기
        self.ground = ground
        pass


    def all_collision(self): # 모든 객체에 대한 충돌 검사
        self.player_collision()
        pass

    def player_collision(self):

        if self.player.CY <= 100:
            self.player.CY = 100

        pass