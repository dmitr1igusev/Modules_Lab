# Dmitrii Gusev
import math


class Shape:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class Circle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def area(self):
        return math.pi * self.x ** 2


class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def area(self):
        return self.y * self.x


class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def area(self):
        return self.y * self.x * 0.5


class Trapezoid(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.z = 0.0

    def set_z(self, z):
        self.z = z

    def area(self):
        return self.z * (self.x + self.y) * 0.5
