import taichi as ti
from dev.object import Black_Hole
from config import width, height
from kernel import render_space, render_bh, make_chunk, copy_grid, update_position, render_r
from dev.object import Orbit


ti.init(arch=ti.cpu)

black_hole = Black_Hole.BlackHole()

black_hole.generate()

orbit = Orbit.Orbit()

blck_h = ti.Vector.field(10,dtype=ti.f32,shape=1)

blck_h[0] = ti.Vector(black_hole.get_params())

blh_chunk = ti.Vector.field(4, dtype=ti.f32, shape=1)

orbit.set_r(blck_h[0][0], blck_h[0][1],blck_h[0][2])

orbit_field = ti.Vector.field(3, dtype=ti.f32, shape=1)

orbit_field[0] = ti.Vector(orbit.get_params())

space_grid = ti.Vector.field(3, dtype=ti.f32, shape=(width, height))

render_space(space_grid, 50)

space = ti.Vector.field(3,dtype=ti.f32,shape=(width, height))

gui = ti.GUI("Taichi Planets", (width, height))

orbit_chunk = ti.Vector.field(4, dtype=ti.f32, shape=1)

make_chunk(orbit_field, orbit_chunk)

while gui.running:
    copy_grid(space_grid, space)
    make_chunk(blck_h, blh_chunk)
    render_bh(space,blck_h, blh_chunk)
    render_r(space, orbit_field, orbit_chunk)
    gui.set_image(space)
    gui.show()