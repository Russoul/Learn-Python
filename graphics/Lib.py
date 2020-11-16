import pyglet
from pyglet.graphics import Batch
from Math import *
from time import time_ns
from typing import Callable, Tuple, List
from pyglet.window import key
from pyglet.gl import *
from functools import reduce #python 3
import operator


def add_line(batch: Batch, origin: Vec2, line: LineSegment, color: Vec3): # [0, 0] -> [width, height]
    batch.add(2, GL_LINES, None,
              ('v2f', (origin + line.start).to_list() + (origin + line.end).to_list()),
              ('c3f', (color.to_list() + color.to_list()))
              )


def addLineUnit(batch: Batch, origin: Vec2, ux, uy, line: LineSegment, color: Vec3):
    batch.add(2, GL_LINES, None,
              ('v2f', [line.start.x * ux + origin.x * ux,
                       line.start.y * uy + origin.y * uy,
                       line.end.x * ux + origin.x * ux,
                       line.end.y * uy + origin.y * uy]),
              ('c3f', (color.to_list() + color.to_list()))
              )
def addTriangleUnit(batch : Batch, origin : Vec2, ux, uy, tri : Triangle, colors : List[Vec3]):
    batch.add(3, GL_TRIANGLES, None,
              ('v2f', [ tri.p0.x * ux + origin.x * ux
                      , tri.p0.y * uy + origin.y * uy
                      , tri.p1.x * ux + origin.x * ux
                      , tri.p1.y * uy + origin.y * uy
                      , tri.p2.x * ux + origin.x * ux
                      , tri.p2.y * uy + origin.y * uy]),
              ('c3f', reduce(operator.concat, map(lambda x: x.to_list(), colors))))
              

def runGraphics( init
               , onMouseMotion : Callable[[float, float, float, float], None]
               , onMousePress : Callable[[float, float, int, int], None]
               , onMouseRelease : Callable[[float, float, int, int], None]
               , onMouseDrag : Callable[[float, float, List[int], int], None]
               , onKeyPress : Callable[[int, int], None]
               , onUpdate : Callable[[Batch, float, float, float, float, float], None]
               , getUnits : Callable[[], Tuple[float, float]]
               , getOrigin : Callable[[], Vec2]):
    window = pyglet.window.Window(resizable=True, vsync=True)
    glClearColor(0.8, 0.8, 0.8, 1.0)
    label = pyglet.text.Label('2D graphics')
    init(window)

    w = window.width
    h = window.height

    mx = 0
    my = 0
    batch = pyglet.graphics.Batch()

    print(f"Window dimensions: width {w}, height {h}")

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        nonlocal mx
        nonlocal my
        mx = x
        my = y
        onMouseMotion(x, y, dx, dy)
    
    @window.event
    def on_mouse_press(x, y, button, mods):
        onMousePress(x, y, button, mods)

    @window.event
    def on_mouse_release(x, y, button, mods):
        onMouseRelease(x, y, button, mods)

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, mods):
        onMouseDrag(x, y, dx, dy, buttons, mods)
   
    @window.event
    def on_key_press(sym, mods):
        onKeyPress(sym, mods)

    fps_display = pyglet.window.FPSDisplay(window=window)

    tx = 0

    def update(dt):
        (unitsX, unitsY) = getUnits()
        nonlocal batch
        batch = pyglet.graphics.Batch()
        w = window.width
        h = window.height
        asp = w / h
        ux = w / unitsX
        uy = h / unitsY
        u = ux  # in case ux = uy

        origin = getOrigin()
        window.set_caption(f"x {(mx - origin.x * ux) / ux:3.2f}, y {(my - origin.y * uy) / uy:3.2f}, ratio {asp:3.3f}")
        onUpdate(batch, dt, w, h, ux, uy)


    @window.event
    def on_draw():
        window.clear()
        batch.draw()
        # fps_display.draw()

    pyglet.clock.schedule_interval(update, 1.0 / 120)
    pyglet.app.run()

