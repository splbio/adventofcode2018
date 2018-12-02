import itertools
import functools
import sys

def get_reduce_trick():
    accumulator = 0
    def reduce_trick(x):
        nonlocal accumulator
        accumulator += x
        return accumulator
    return reduce_trick

print(
  next(
    itertools.islice(
      filter(
        lambda x, m={}: m.setdefault(x, False) if not x in m else True,
        map(
          get_reduce_trick(),
          itertools.cycle(map(int, sys.stdin.readlines()))
        ),
      ),
      1
    )
))
