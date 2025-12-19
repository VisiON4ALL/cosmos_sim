import math
import random

class Orbit:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.r = 0.0

    def set_r(self, x,y,z):
        self.x = x
        self.y = y
        self.r = z*10

    def get_params(self):
        return [self.x,self.y,self.r]