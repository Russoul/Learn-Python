from Lib import *

def doNothing():
   pass

def setUnits():
    return (100, 100)


# Screen Space:
#  Y
#  ^             (w, h)
#  |
#  |
#  |
#  |
#  |
#  --------------> X
# (0, 0)                 

t = 0
window = ()

def setOrigin():
    return Vec2(50, 50)

def onUpdate(batch, dt, w, h, ux, uy): # render data, delta time, width, height,
                                       #one unit along X in Screen Space,
                                       #one unit along Y in Screen Space
   r = w / h
   origin = setOrigin()
   global t
   red = Vec3(1, 0, 0)
   green = Vec3(0, 1, 0)
   blue = Vec3(0, 0, 1)
   yellow = red + green
   white = red + green + blue
   gray = white * 0.2
   black = Vec3(0, 0, 0)
   addLineUnit(batch, Vec2(0, 0), ux, uy,
            LineSegment(Vec2(0, origin.y), Vec2(w, origin.y)), gray)
   addLineUnit(batch, Vec2(0, 0), ux, uy,
            LineSegment(Vec2(origin.x, 0), Vec2(origin.x, h)), gray)
   p0 = 20         
   px = -1 * ( p0 + 2 * t + 1 * t*t / 2) # Px = Px₀ + Vx₀t + Ax * t²/2
   addLineUnit(batch, origin, ux, uy, LineSegment(Vec2(px, 25), Vec2(px, 45)), yellow)
   t = t + dt # t += dt
   addTriangleUnit(batch, origin, ux, uy, Triangle(Vec2(px, 15), Vec2(10 + px, 0), Vec2(-10 + px, 0)), [red, green, blue])
   addLineUnit(batch, origin, ux, uy, LineSegment(Vec2(1, 0.5 * r), Vec2(1, -0.5 * r)), black)
   addLineUnit(batch, origin, ux, uy, LineSegment(Vec2(0.5, 1), Vec2(-0.5, 1)), black)

def setup(thisWindow):
    global window
    window = thisWindow


def myStupidFunc(f, x):
    return f(x)

def plusOne(x):
    return x + 1

def squared(x):
    t = x ** 2
    return x ** 2

myEmptyList = []
myList2 = Vec2(1, 2).to_list()
myList1 = [1, Vec2(2, 3), "hi"]
print("hi")

runGraphics(
             init = setup
           , onMouseMotion = lambda x, y, dx, dy : ()
           , onKeyPress = lambda sym, mods : print("key press", sym)
           , onMousePress = lambda x, y, but, mods : print("mouse press", but, mods)
           , onMouseRelease = lambda x, y, but, mods : ()
           , onMouseDrag = lambda x, y, dx, dy, buts, mods : ()
           , onUpdate = onUpdate
           , getUnits = setUnits
           , getOrigin = setOrigin)

