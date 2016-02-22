# -*- coding: utf-8 -*-
from math import sqrt

while 1:
    line = raw_input()

    if len(line) == 1:
        break

    a, b, c = [int(x) for x in line.split()]

    print '%d' % sqrt(a * b * 100 / c)
