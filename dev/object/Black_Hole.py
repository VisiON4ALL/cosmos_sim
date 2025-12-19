import math
from objects.spaceObject import SpaceObject
from config import G, v_max, k, width, height
import random

class BlackHole(SpaceObject):
    def __init__(self):
        super().__init__()
        self.r2=0.0  # радиус горизонта событий
        self.r3=0.0  # радиус аккреционного диска
        self.r4=0.0  # радиус гравитационного влияния
        self.color = [1.0, 0.0, 0.0] # индекс 7, 8 ,9

    def generate(self):
        self.r = random.uniform(10.0, 50.0)
        self.r2 = self.r * 1.2
        self.r3 = self.r * 2.0
        self.r4 = self.r * 5.0

        self.x = random.uniform(self.r4, width - self.r4)
        self.y = random.uniform(self.r4, height - self.r4)

        self.m = self.r ** 5

        self.v = 0.0
        self.vx = 0.0
        self.vy = 0.0

    def get_params(self):
        return [self.x, self.y, self.r, self.r2, self.r3, self.r4, self.m, self.color[0], self.color[1], self.color[2]]