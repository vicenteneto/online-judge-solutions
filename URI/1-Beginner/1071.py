# -*- coding: utf-8 -*-

x, y = [int(raw_input()) for i in range(2)]

if x > y:
    x, y = y, x

if x % 2 == 1:
    x += 2
else:
    x += 1

print sum([i for i in range(x, y, 2)])
