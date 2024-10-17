from pico2d import*

class CupheadBainging:
    def __init__(self):
        Path = 'PlayerResoures/Idle/cuphead_idle_000'
        self.image_Idle = []
        for a in range(1,5+1):
            FinalPath = Path + str(a)
            self.image_Idle.append(load_image(FinalPath + '.png'))


        self.MaxFrame = [5]



    def update(self):
        pass

    def late_update(self):
        pass

    def render(self):

        pass