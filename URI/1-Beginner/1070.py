# -*- coding: utf-8 -*-

x = int(raw_input())
x += 1 if x % 2 == 0 else 0

for i in range(x, x + 11, 2):
    print i
