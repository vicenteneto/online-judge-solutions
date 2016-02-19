# -*- coding: utf-8 -*-

while 1:
    x = int(raw_input())

    if not x:
        break

    x += 0 if x % 2 == 0 else 1

    print sum([v for v in range(x, x + 9, 2)])
