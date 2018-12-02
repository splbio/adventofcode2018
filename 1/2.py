#!/bin/env python3

import sys
import itertools

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
