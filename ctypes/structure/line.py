#!/usr/bin/env python
import ctypes

from point import Point


class Line(ctypes.Structure):
    _fields_ = [
        ('start', Point),
        ('end', Point)
    ]

    lib = ctypes.CDLL("libline.so")

    def __init__(self):
        self._get_line = self.lib.get_line
        self._get_line.restype = Line

        self._show_line = self.lib.show_line
        self._show_line.argtypes = [Line]

        self._move_line = self.lib.move_line
        self._move_line.argtypes = [ctypes.POINTER(Line)]

        line = self._get_line()
        self.start = line.start
        self.end = line.end

    def __repr__(self):
        return '{0}->{1}'.format(self.start, self.end)

    def show_line(self):
        self._show_line(self)

    def move_line(self):
        self._move_line(self)


if __name__ == '__main__':
    print("Move Line in Python")
    line = Line()
    print("Line in Python is ", line)
    line.move_line()
    print("Line in Python is ", line)
