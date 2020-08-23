from math import *

Pi = 3.14159265359


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{{{self.x}, {self.y}}}"

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return self.x * other.x + self.y * other.y
        else:
            return Vec2(self.x * other, self.y * other)

    def length(self):
        sqrt(self * self)

    def angle(self, other):
        return acos(self * other / self.length() / other.length()) * 180 / Pi

    def to_list(self):
        return [self.x, self.y]

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{{{self.x}, {self.y}, {self.z}}}"

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

    def length(self):
        sqrt(self * self)

    def angle(self, other):
        return acos(self * other / self.length() / other.length()) * 180 / Pi

    def to_list(self):
        return [self.x, self.y, self.z]


class LineSegment:
    def __init__(self, start: Vec2, end: Vec2):
        self.start = start
        self.end = end

class Triangle:
    def __init__(self, p0 : Vec2, p1 : Vec2, p2 : Vec2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
