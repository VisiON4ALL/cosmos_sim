class SpaceObject:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.r = 0.0
        self.m = 0.0
        self.v = 0.0
        self.vx = 0.0
        self.vy = 0.0

    def generate(self):
        """
        Метод, который создаёт параметры объекта.
        В базовом классе можно оставить NotImplementedError,
        чтобы наследники обязательно его переопределяли.
        """
        raise NotImplementedError("Метод generate() должен быть реализован в наследнике")

    def get_params(self):
        """
           Возвращает параметры в виде списка или вектора,
           чтобы их можно было передать в Taichi поле.
        """
        return [self.x, self.y, self.r, self.m, self.v, self.vx, self.vy]