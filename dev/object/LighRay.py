class LighRay():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0  # движение по X
        self.vy = 0.0  # движение по Y
        self.length = 10.0  # длина луча
        self.color = [1.0, 1.0, 0.5]  # светло-жёлтый
        self.trail = 5  # сколько пикселей след оставить

    def generate(self, start_x, start_y, speed):
        self.x = start_x
        self.y = start_y
        self.vx = 0.0
        self.vy = speed  # направлено вниз