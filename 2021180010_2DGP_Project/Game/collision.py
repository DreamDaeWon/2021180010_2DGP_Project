from Game.Effect import player_hand_hit_effect
from Game.UI import player_skill_ui
from Game.UI.player_skill_ui import Player_Skill_Ui
from dw_define import*

import object_manager

import Effect.player_hand_hit_effect

class Collision:
    def __init__(self):
        self.all_object = None # 모든 객체를 받아올 것임

        self.player = None # 플레이어 객체를 받아올 것임

        #self.player_bullet = None # 플레이어 총알 객체 리스트를 받아올 것임

        self.boss = None # 보스 객체를 받아 올 것임

        #self.boss_bullet = None # 보스의 총알 객체 리스트를 받아올 것임

        self.ground = None # 땅 받아오기

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
        #self.player_collision()
        #self.boss_collision()
        #self.boss_bullet_collision()
        #self.boss_bullet_item_collision()
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

        if self.boss != None:
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

    def player_skill_collision(self): # 보스가 맞는 거임 # 이거 수정하고 추가해야 함

        for o in object_manager.world[object_manager.player_skill_list_num]:
            if o.CX + o.get_collision_size()[0] < 0:
                o.this_delete = True

            elif self.box_collision(self.boss.get_collision_size(),o.get_collision_size()):
                self.boss.hit_bool = True
                o.this_delete = True

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
                if self.player.skill_number < 3:
                    self.player.skill_number += 1
                    skill = Player_Skill_Ui(self.player.skill_number)
                    object_manager.world[object_manager.UI_list_num].append(skill)

                effect = player_hand_hit_effect.Player_hand_hit_effect()
                effect.CX = self.player.CX
                effect.CY = self.player.CY
                object_manager.world[object_manager.effect_num].append(effect)
                o.this_delete = True


        pass


World_collision = Collision()