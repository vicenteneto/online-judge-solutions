# -*- coding: utf-8 -*-

x = int(raw_input())

if x % 2 == 0:
    x += 1

for i in range(x, x + 11, 2):
    print i
