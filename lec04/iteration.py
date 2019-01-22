"""our first loop!

This file demonstates two design strategies:

 - Iteration over a range of ints

 - Composing smaller functions into larger ones

"""

from typing import Optional
from typing import Callable, Iterable


def substr_index(needle: str, haystack: str) -> Optional[int]:
    """Returns the first index in `haystack` where `needle` may be
    found, or None if `needle` is not a substring of `haystack`.

    >>> substr_index('a', 'apple')
    0
    >>> substr_index('l', 'apple')
    3
    >>> substr_index('g', 'apple')
    >>> substr_index('pl', 'apple')
    2
    """

    3
