"""Bigrams are pairs of adjacent words."""

import random
from enum import Enum, auto
from typing import List, Tuple

from lib230 import record, Factory


_Bigram = Tuple[str, str]


def _bigrams_in(text: List[str]) -> List[_Bigram]:
    """Turns a list of strings into its list of bigrams.

    >>> _bigrams_in(['a', 'b', 'c', 'd'])
    [('a', 'b'), ('b', 'c'), ('c', 'd')]
    """
    return [(text[i], text[i + 1])
            for i in range(len(text) - 1)]


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


