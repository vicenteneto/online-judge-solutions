# -*- coding: utf-8 -*-

x, y = [int(raw_input()) for x in range(2)]

if x > y:
    x, y = y, x

print sum([x for x in range(x, y + 1) if x % 13 != 0])
