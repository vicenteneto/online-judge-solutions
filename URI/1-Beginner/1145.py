# -*- coding: utf-8 -*-

x, y = [int(x) for x in raw_input().split()]

for i in range(1, y + 1, x):
    sequence = ""
    for j in range(i, i + x):
        sequence += '%d ' % j
    print sequence[:-1]
