# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    x, y = [int(x) for x in raw_input().split()]

    if x > y:
        x, y = y, x

    x += 1 if x % 2 == 0 else 2
    print sum([j for j in range(x, y, 2)])
