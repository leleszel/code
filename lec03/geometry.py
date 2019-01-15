"""Some computational geometry."""

from math import sqrt
from typing import NamedTuple

# 1. Data definitions
# 2. Header (name, signature, purpose)
# 3. Examples
# 4. Body
# 5. Testing


def sqr(x: float) -> float:
    """Computes the square of the given number.

    >>> sqr(0)
    0
    >>> sqr(5)
    25
    """
    return x * x


class Employee(NamedTuple):
    """Represents an employee."""
    name:          str
    id:            int
    supervisor_id: int
    salary:        int


class Position(NamedTuple):
    """Represents a 2-D position.

    >>> P = Position(3, 4)
    >>> Q = Position(3.5, -9)
    >>> P.x
    3
    >>> Q.y
    -9
    """
    x: float
    y: float


def distance(p1: Position, p2: Position) -> float:
    """Computes the Euclidean distance between two positions.

    >>> distance(Position(0, 0), Position(0, 0))
    0.0
    >>> distance(Position(0, 0), Position(3, 4))
    5.0
    """
    return sqrt(sqr(p2.x - p1.x) + sqr(p2.y - p1.y))


def manhattan_distance(p1: Position, p2: Position) -> float:
    """Computes a Manhattan distance.

    >>> manhattan_distance(Position(0, 0), Position(3, 4))
    7
    >>> manhattan_distance(Position(0, 0), Position(1, 1))
    2
    """
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)



