# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    x = int(raw_input())

    if x == sum([j for j in range(1, int(x / 2) + 1) if x % j == 0]):
        print x, 'eh perfeito'
    else:
        print x, 'nao eh perfeito'
