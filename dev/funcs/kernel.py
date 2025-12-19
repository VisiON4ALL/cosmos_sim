import taichi as ti

@ti.kernel
def make_chunk(field: ti.template(), chunk: ti.template() ) :
    x_min = field[0][0] - field[0][2] #x - r
    y_min = field[0][1] - field[0][2] #y - r
    x_max = field[0][0] + field[0][2] #x + r
    y_max = field[0][1] + field[0][2] #y + r
    chunk[0] = ti.Vector([x_min,y_min,x_max,y_max])

@ti.func
def is_inside_circle(i, j, vec):
    dx = i - vec[0]
    dy = j - vec[1]
    return dx ** 2 + dy ** 2 <= vec[2] ** 2

@ti.kernel
def render_space(field: ti.template(), grid_size: ti.i32) :
    for i, j in field:
        if i % grid_size == 0 or j % grid_size == 0 :
            field[i,j] = ti.Vector([1.0,1.0, 1.0])
        else:
            field[i,j] = ti.Vector([0.0,0.0,0.0])

@ti.kernel
def render_bh(field: ti.template(), obj: ti.template(), chunk: ti.template()) :
    for i in range(int(chunk[0].x), int(chunk[0].z)):
        for j in range(int(chunk[0].y), int(chunk[0].w)):
            if is_inside_circle(i, j, obj[0]):
                r = obj[0][7]
                g = obj[0][8]
                b = obj[0][9]
                field[i, j] = ti.Vector([r, g, b])


@ti.kernel
def copy_grid(grid: ti.template(), frame: ti.template()):
    for i, j in frame:
        frame[i, j] = grid[i, j]

@ti.kernel
def update_position(field: ti.template(), obj: ti.template()):
        obj[0][0] +=2
        obj[0][1] +=2



@ti.func
def dia(i:int, j:int, obj: ti.template()):
    dx = i - obj[0]
    dy = j - obj[1]
    dist = ti.sqrt(dx * dx + dy * dy)
    return obj[2] - 2 <= dist <= obj[2] + 2

@ti.kernel
def render_r(field: ti.template(), obj: ti.template(), chunk: ti.template()) :
    for i in range(int(chunk[0].x), int(chunk[0].z)):
        for j in range(int(chunk[0].y), int(chunk[0].w)):
            if dia(i, j, obj[0]):
                r = 0
                g = 1
                b = 0
                field[i, j] = ti.Vector([r, g, b])