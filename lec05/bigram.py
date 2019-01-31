"""Bigrams are pairs of adjacent words."""

import random
from enum import Enum, auto
from typing import List, Tuple

from lib230 import record, Factory


# `is` versus `==`
@record
class Foo:
    """Foo.

    >>> f1 = Foo(3, 4)
    >>> f2 = Foo(3, 4)
    >>> f3 = Foo(4, 5)
    >>> f4 = f1
    >>> f1 is f1
    True
    >>> f2 is f2
    True
    >>> f1 is f4
    True
    >>> f1 is f2
    False
    >>> f1 == f2
    True
    """
    a: int
    b: int


_Bigram = Tuple[str, str]


def _bigrams_in(text: List[str]) -> List[_Bigram]:
    """Turns a list of strings into its list of bigrams.

    >>> _bigrams_in(['a', 'b', 'c', 'd'])
    [('a', 'b'), ('b', 'c'), ('c', 'd')]
    >>> _bigrams_in(['a', 'b', 'a', 'b', 'c', 'd'])
    [('a', 'b'), ('b', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'd')]
    """
    return [(text[i], text[i + 1])
            for i in range(len(text) - 1)]

    # # Longer but equivalent to above:
    # result = []
    # for i in range(len(text) - 1):
    #     result.append((text[i], text[i + 1]))
    # return result


@record
class BigramModel:
    """A Markov model of bigrams."""

    _all_bigrams: List[_Bigram] = Factory(list)

    def __len__(self) -> int:
        """Returns the number of bigrams in the model.

        >>> m = BigramModel()
        >>> len(m)
        0
        >>> m.train_one('a', 'b')
        >>> len(m)
        1
        >>> m.train_one('a', 'b')
        >>> len(m)
        2
        """
        return len(self._all_bigrams)

    def next(self, state: str) -> str:
        """Produces the next word from the current word.

        >>> m = BigramModel()
        >>> m.train_one('one', 'two')
        >>> m.train_one('two', 'three')
        >>> m.train_one('two', 'three')
        >>> m.next('two')
        'three'
        """
        return random.choice(self._possibilities(state))

    def _possibilities(self, state: str) -> List[str]:
        """Returns a list of all possible next words at
        the appropriate frequencies.

        >>> m = BigramModel()
        >>> m.train('a bee a bee a bee a cow'.split())
        >>> m._possibilities('a')
        ['bee', 'bee', 'bee', 'cow']
        >>> m._possibilities('cow')
        []
        """
        result = []
        for bg in self._all_bigrams:
            if bg[0] == state:
                result.append(bg[1])
        return result

    def babble(self, n: int, start: str = '', stop: str = '') -> List[str]:
        """Produces a sequence of words randomly from the model.

        >>> m = BigramModel()
        >>> m.train(['', 'a', 'b', 'c', ''])
        >>> m.babble(6)
        ['', 'a', 'b', 'c', '', 'a', 'b', 'c', '']
        >>> m.babble(6, 'b', 'a')
        ['b', 'c', '', 'a', 'b', 'c', '', 'a']
        """
        state = start
        result = [state]
        while state != stop or len(result) < n:
            state = self.next(state)
            result.append(state)
        return result

    def check(self, text: List[str]) -> bool:
        """Returns whether `text` could have been generated
        by `self`.

        >>> m = BigramModel()
        >>> m.train('a b a c a'.split())
        >>> m.check('a b a b a b a'.split())
        True
        >>> m.check('a b a b c b a'.split())
        False
        """
        for (fst, snd) in _bigrams_in(text):
            if not self.check_one(fst, snd):
                return False
        return True


    def train(self, corpus: List[str]) -> None:
        """Trains the model on a whole corpus text.

        >>> m = BigramModel()
        >>> len(m)
        0
        >>> m.train(['a', 'b', 'a', 'c', 'a'])
        >>> len(m)
        4
        """
        self._all_bigrams.extend(_bigrams_in(corpus))

    def check_one(self, fst: str, snd: str) -> bool:
        """Returns whether (fst, snd) is in this model.

        >>> m = BigramModel()
        >>> m.train('a b a c a'.split())
        >>> m.check_one('a', 'b')
        True
        >>> m.check_one('c', 'b')
        False
        """
        return (fst, snd) in self._all_bigrams

    def train_one(self, fst: str, snd: str) -> None:
        """Adds one bigram to this model.

        >>> m = BigramModel()
        >>> len(m)
        0
        >>> m.train_one('goodnight', 'world')
        >>> len(m)
        1
        >>> m.train_one('world', 'goodnight')
        >>> len(m)
        2
        >>> m.train_one('goodnight', 'moon')
        """
        self._all_bigrams.append((fst, snd))


