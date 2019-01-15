from math import sqrt

from geometry import *


def test_distance():
    a = Position(0, 0)
    b = Position(3, 4)
    c = Position(1, 1)
    assert distance(a, a) == 0
    assert distance(a, b) == 5
    assert distance(a, c) == sqrt(2)


def test_manhattan_distance():
    a = Position(0, 0)
    b = Position(3, 4)
    c = Position(1, 1)
    assert manhattan_distance(a, a) == 0
    assert manhattan_distance(a, b) == 7
    assert manhattan_distance(a, c) == 2

