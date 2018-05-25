import math

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magSqd(self):
        return self.x*self.x + self.y*self.y

    def mag(self):
        return math.sqrt(self.magSqd())

    def heading(self):
        return math.atan2(self.y, self.x)

    def leftNormal(self):
        return Vec2(-self.y, self.x)

    def rightNormal(self):
        return Vec2(self.y, -self.x)

    def norm(self):
        m = self.mag()
        self.x /= m
        self.y /= m

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def setMag(self, mag):
        self.norm()
        self.scale(mag)

    @staticmethod
    def dot(v1, v2):
       return float(v1.x * v2.x + v1.y * v2.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __isub(self, other):
        self.x -= other.x
        self.y -= other.y

    def __imul__(self, scalar):
        self.scale(scalar);

    def __idiv__(self, scalar):
        self.scale(1.0/scalar);

    def __add__(self, other):
       return Vec2(self.x + other.x, self.y + other.y)

    def __add__(self, other):
       return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
       return Vec2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
       return Vec2(self.x / scalar, self.y / scalar)
    