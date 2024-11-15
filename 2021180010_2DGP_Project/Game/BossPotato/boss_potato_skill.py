from pico2d import*

import os
import sys


# 현재 파일의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 파일의 한 단계 위 디렉터리를 가져옵니다
parent_dir = os.path.dirname(current_dir) # 부모 디렉터리를 시스템 경로에 추가합니다
sys.path.append(parent_dir) # 이제 'frametime' 모듈을 가져올 수 있습니다
import frametime


class Boss_potato_skill:

    def __init__(self):

        self.CX = 0.0
        self.CY = 0.0

        self.rx = 0.0
        self.ry = 0.0

        self.frame = 0.0

        self.now_state_dict = 0

        pass


    def in_put_resources(self):
        # 리소스 기본상태
        path = 'BossPotato/PotatoResource/BossPotato.png'  # main.py 기준임
        self.image = load_image(path)
        # 한 사진당
        # 0 가로크기, 1 세로크기, 2 총 몇 프레임인지?, 3 가로 프레임 몇 개인지?, 4 세로 프레임 몇 개인지?, 5 마지막 줄 가로 프레임,
        # 6 x값 어디서부터 시작하는지?, 7 y값 어디서부터 시작하는지?, 8 x값 얼마만큼 떨어지는지? , 9 y값 얼마만큼 떨어지는지?

        # 여기에 이미지 관련 정보 set 함수 적기

        # 보스 intro 모션
        self.set_attack_motion()

        # 보스 일반 공격 모션

