#!/bin/env python3

import sys

in_data = sys.stdin.readlines()
freq = 0
seen_freq = {}
while True:
    for x in in_data:
        freq += int(x)
        """
        print("{} {}".format(x, freq))
        import time
        time.sleep(0.1)
        """
        if freq in seen_freq:
            print(freq)
            sys.exit(0)
        seen_freq[freq] = True
