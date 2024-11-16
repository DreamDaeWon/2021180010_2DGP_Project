from dw_define import*

import object_manager

class Collision:
    def __init__(self):
        self.all_object = 0 # 모든 객체를 받아올 것임

        self.player = 0 # 플레이어 객체를 받아올 것임

        self.player_bullet = 0 # 플레이어 총알 객체 리스트를 받아올 것임

        self.boss = 0 # 보스 객체를 받아 올 것임

        self.boss_bullet = 0 # 보스의 총알 객체 리스트를 받아올 것임

        self.ground = 0 # 땅 받아오기

        pass


    def box_collision(self,a,b):

        if a[2] > b[0] and a[0] < b[2] and a[1] > b[3] and a[3] < b[1]:
            return True
        else:
            return False

        pass


    def get_player(self, player): # 플레이어 받아오기
        self.player = player
        pass

    def get_boss(self, boss):  # 보스 받아오기
        self.boss = boss
        pass

    def get_ground(self, ground):  # 땅 받아오기
        self.ground = ground
        pass


    def all_collision(self): # 모든 객체에 대한 충돌 검사
        self.player_collision()
        self.boss_collision()
        self.boss_bullet_collision()
        pass

    def player_collision(self):
        if self.player == None:
            return

        if self.player.get_collision_size()[3] < 50:
            self.player.CY = 50 + self.player.player_ry
            self.player.gravity = False
            self.player.jumping = False
            self.player.normal_attaking = False
            self.player.jump_angle = 0
            self.player.normal_attaking_angle = 0


        if self.player.get_collision_size()[0] <= 0.0:
            self.player.CX = 0.0 + self.player.player_rx

        if self.player.get_collision_size()[2] >= 1100:
            self.player.CX = 1100 - self.player.player_rx

        if self.box_collision(self.player.get_collision_size(),self.boss.get_collision_size()):
            if not self.player.normal_attaking and self.boss.shoot == True:
                self.player.hit_bool = True


        pass

    def boss_collision(self):

        if self.boss == None:
            return

        if self.boss.get_collision_size()[3] < 50:
            self.boss.CY = 50 + self.boss.boss_potato_ry


        pass

    def boss_bullet_collision(self):

        for o in object_manager.world[3]:
            if o.CX + o.get_collision_size()[0] < 0:
                o.this_delete = True

            elif self.box_collision(self.player.get_collision_size(),o.get_collision_size()):
                self.player.hit_bool = True
                o.this_delete = True


        pass

    def boss_bullet_item_collision(self):

        for o in object_manager.world[object_manager.player_skill_item_num]:
            if o.CX + o.get_collision_size()[0] < 0:
                o.this_delete = True

            elif self.box_collision(self.player.get_collision_size(),o.get_collision_size()):
                self.player.hit_bool = True
                o.this_delete = True


        pass