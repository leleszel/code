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


def test_circle_area():
    c = Circle(Position(0, 0), 4)
    assert c.area() == 16 * pi


def test_rectangle_area():
    r = Rectangle(Position(0, 0), 4, 6)
    assert r.area() == 24


def test_circle_contains():
    c = Circle(Position(0, 0), 1)
    p = Position(.3, .2)
    q = Position(1.3, .2)
    assert c.contains(p)
    assert not c.contains(q)


def test_rectangle_contains():
    r = Rectangle(Position(-1, -1), 2, 2)
    p = Position(.5, .5)
    q = Position(1.5, .5)
    assert r.contains(p)
    assert not r.contains(q)


