# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    x, y = [int(v) for v in raw_input().split()]

    x += 1 if x % 2 == 0 else 0

    print sum([v for v in range(x, x + y * 2, 2)])
