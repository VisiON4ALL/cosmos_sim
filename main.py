import random
import numpy as np
import taichi as ti
from objects.spaceObject import SpaceObject
from objects.planet import Planet
from taichi_kernels.render import make_chunks, fill_image
from config import G, v_max

ti.init(arch=ti.cpu)
width, height = 1270, 1024
n_circles = random.randint(1, 10)

objects = [Planet() for _ in range(n_circles)]
for obj in objects:
    obj.generate()  # генерируем параметры

centers_np = np.array([obj.get_params() for obj in objects], dtype=np.float32)

chunks = ti.Vector.field(4, dtype=ti.f32, shape=n_circles)
centers = ti.Vector.field(6, dtype=ti.f32, shape=n_circles)

for i in range(n_circles):
    centers[i] = centers_np[i]

gray_scalar_img = ti.field(dtype=ti.f32, shape=(width, height))

make_chunks(centers, chunks, n_circles)

fill_image(centers, chunks, gray_scalar_img, n_circles)

gui = ti.GUI("Taichi Planets", (width, height))
while gui.running:
    gui.set_image(gray_scalar_img)
    gui.show()
