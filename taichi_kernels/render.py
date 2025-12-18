import taichi as ti

@ti.func
def is_inside_circle(i, j, vec):
    dx = i - vec[0]
    dy = j - vec[1]
    return dx**2 + dy**2 <= vec[2]**2

@ti.kernel
def make_chunks(centers: ti.template(), chunks: ti.template(), n: ti.i32):
    for k in range(n):
        x_min = centers[k].x - centers[k].z #x
        y_min = centers[k].y - centers[k].z #y
        x_max = centers[k].x + centers[k].z #z
        y_max = centers[k].y + centers[k].z #w
        chunks[k] = ti.Vector([x_min, y_min, x_max, y_max])

@ti.kernel
def fill_image(centers: ti.template(), chunks: ti.template(), gray_scalar_img: ti.template(), n: ti.i32):
    for k in range(n):
        for i in range(int(chunks[k].x), int(chunks[k].z)):
            for j in range(int(chunks[k].y), int(chunks[k].w)):
                if is_inside_circle(i, j, centers[k]):
                    gray_scalar_img[i, j] = 1.0
