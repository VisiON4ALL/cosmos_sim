import random
import taichi as ti

ti.init(arch=ti.cpu)

width, height = 1270, 1024
max_radius = 50
n_circles = random.randint(1, 10)

gray_scalar_img = ti.field(dtype=ti.f32, shape=(width, height))

centers = ti.Vector.field(4, dtype=float, shape = n_circles)
chunks = ti.Vector.field(4, dtype=float, shape = n_circles)


@ti.kernel
def fill_cts():
    for i in range(n_circles):
        r = ti.random() * max_radius
        x = r + ti.random() * (width - 2*r)
        y = r + ti.random() * (height - 2*r)
        m = i * r**3
        centers[i] = ti.Vector([x, y, r, m])

fill_cts()

@ti.kernel
def make_chunks():
    for k in range(n_circles):
        x_min = centers[k].x - centers[k].z #x
        y_min = centers[k].y - centers[k].z #y
        x_max = centers[k].x + centers[k].z #z
        y_max = centers[k].y + centers[k].z #w
        chunks[k] = ti.Vector([x_min, y_min, x_max, y_max])

make_chunks()

@ti.func
def is_inside_circle(i,j, vec):
    dx = i - vec[0]
    dy = j - vec[1]
    return dx**2 + dy**2 <= vec[2]**2


@ti.kernel
def fill_image():
    for k in range(n_circles):
        for i in range(int(chunks[k].x), int(chunks[k].z)):
           for j in range(int(chunks[k].y), int(chunks[k].w)):
               if is_inside_circle(i,j,centers[k]):
                   gray_scalar_img[i,j] = 1.0

fill_image()
gui = ti.GUI('gray scalar image random valuues', (width, height))
while gui.running:
    gui.set_image(gray_scalar_img)
    gui.show()
