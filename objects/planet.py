import math
from objects.spaceObject import SpaceObject
from config import G, v_max, k

class Planet(SpaceObject):
    def __init__(self):
        super().__init__()

    def generate(self):
        # Простейший пример генерации
        import random
        self.r = random.uniform(5.0, 50.0)   # радиус
        self.x = random.uniform(self.r, 1270 - self.r)  # координата X
        self.y = random.uniform(self.r, 1024 - self.r)  # координата Y
        self.m = self.r ** 3  # масса пропорциональна объёму
        self.v = min(v_max, k * G * self.m)
        angle = random.uniform(0.0, 2.0 * math.pi)
        self.vx = math.cos(angle) * self.v
        self.vy = math.sin(angle) * self.v