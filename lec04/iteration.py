"""Our first loop!

This file demonstates two design strategies:

 - Iteration over a range of ints

 - Composing smaller functions into larger ones

"""

from typing import Optional
from typing import Callable, Iterable


# "Helper function" for substr_index.
def _matches_at(needle: str, haystack: str, base: int) -> bool:
    if len(needle) + base > len(haystack):
        return False
    for i in range(len(needle)):
        if needle[i] != haystack[base + i]:
            return False
    return True


def substr_index(needle: str, haystack: str) -> Optional[int]:
    for i in range(len(haystack)):
        if _matches_at(needle, haystack, i):
            return i
    return None

