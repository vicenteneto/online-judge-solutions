# -*- coding: utf-8 -*-

x, y = [int(raw_input()) for i in range(2)]

if x > y:
    x, y = y, x

x += 2 if x % 2 == 1 else 1

print sum([i for i in range(x, y, 2)])
