# -*- coding: utf-8 -*-

# logging
import logging
logger = logging.getLogger(__name__)
logger.debug(f'MODULE {__name__}')

import collections

__all__ = ['CyclerIterator']

# ------------------------------------------------------------------------------

class CyclerIterator :

    def __init__(self, iterable) :
        self._cache = collections.deque(enumerate(iterable))
        self._backward = False

    @property
    def cachesize(self) :
        return len(self._cache)

    @property
    def index(self) :
        if self.cachesize > 0 :
            return self._cache[0][0]

    @property
    def backward(self) :
        return self._backward

    @backward.setter
    def backward(self, backward) :
        state = self._backward
        self._backward = bool(backward)
        # changement de sens ?
        if state != self._backward :
            next(self)

    def __next__(self) :
        if self.cachesize > 0 :
            if self.backward :
                current = self._cache.pop()
                self._cache.appendleft(current)
            else :
                current = self._cache.popleft()
                self._cache.append(current)

            return current

    def reverse(self) :
        self.backward = not self.backward

    def skip(self, number) :
        for n in range(number) :
            current = next(self)
            logger.debug(f'skip: current={current}')

    def first(self) :
        # mémoriser la direction
        direction = self.backward
        stop = 1 if direction else self.cachesize - 1

        # remonter jusqu'au premier élément (juste avant)
        self.backward = True
        while True :
            current = next(self)
            logger.debug(f'first: current={current}')
            if current is None or current[0] == stop :
                break

        # rétablir la direction
        self.backward = direction

    def last(self) :
        # mémoriser la direction
        direction = self.backward
        stop = 0 if direction else self.cachesize - 2

        # avancer jusqu'au dernier élément (juste avant)
        self.backward = False
        while True :
            current = next(self)
            logger.debug(f'last: current={current}')
            if current is None or current[0] == stop :
                break

        # rétablir la direction
        self.backward = direction
