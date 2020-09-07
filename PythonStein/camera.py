import math


class Camera:
    def __init__(self, pos, dir, fov):
        self.pos = pos
        self.dir = dir
        self.fov = fov

        radians = self.fov*(math.pi/180)
        p = math.fabs(
            math.sqrt(self.dir[0]**2 + self.dir[1]**2)) * math.tan(radians/2)

        if self.dir[0] == 0:
            self.plane = [p, 0]
        else:
            self.plane = [0,p]