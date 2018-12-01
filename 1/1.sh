#!/bin/sh

python3 -c 'import sys;print(sum([int(x) for x in sys.stdin.readlines()]))' < input.txt
