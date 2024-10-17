from pico2d import*


class CupheadBainging:
    def __init__(self):
        self.frame = 0

        path = 'CupHeadBanging/PlayerResoures/Idle/cuphead_idle_000' # main.py 기준임
        self.image_Idle = []
        for a in range(1,5+1):
            finalPath = path + str(a) + '.png'
            self.image_Idle.append(load_image(finalPath))


        self.maxFrame = 5



    def update(self):
        self.frame += 1
        if self.frame >= self.maxFrame:
            self.frame = 0

        pass

    def late_update(self):

        pass

    def render(self):
        self.image_Idle[self.frame].draw(100,100)
        pass