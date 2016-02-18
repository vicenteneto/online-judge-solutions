# -*- coding: utf-8 -*-

x, y = [int(raw_input()) for i in range(2)]

if x > y:
    x, y = y, x

for i in range(x + 1, y):
    rest = i % 5
    if rest == 2 or rest == 3:
        print i
