#!/usr/bin/env python
import ctypes


class Point(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]

    lib = ctypes.CDLL("libpoint.so")

    def __init__(self, x=None, y=None):
        assert (x is None) == (y is None)

        self._get_point = self.lib.get_point
        self._get_point.restype = Point

        self._show_point = self.lib.show_point
        self._show_point.argtypes = [Point]

        self._move_point = self.lib.move_point
        self._move_point.argtypes = [ctypes.POINTER(Point)]

        if x is None:
            self.x = x
            self.y = y
        else:
            point = self._get_point()
            self.x = point.x
            self.y = point.y

    def __repr__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def show_point(self):
        self._show_point(self)

    def move_point(self):
        self._move_point(self)


if __name__ == '__main__':
    a = Point(5, 6)
    print("Point in Python is", a)
    a.show_point()
    a.move_point()
    print("Point in Python is", a)
