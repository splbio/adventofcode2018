import itertools

import sys
import itertools

"""
freq = 0
seen_freq = {}
for x in itertools.cycle(sys.stdin.readlines()):
    freq += int(x)
    if freq in seen_freq:
        break
        #print(freq)
        #sys.exit(0)
    seen_freq[freq] = True
print(freq)
"""

def f(x, m={}):
    print("{}".format(x))
    return m.setdefault(x, False) if not x in m else True

print(
  next(itertools.islice(
    itertools.ifilter(
        #lambda x, m={}: m.setdefault(x, False) if not x in m else True,
        f,
        itertools.imap(
            lambda x, y: y[0] := y[0] + x,
            itertools.cycle(sys.stdin.readlines())),
            itertools.repeat([0])
        )
    1
    )
))

# print(next(itertools.islice(itertools.cycle([5]), 3)))
