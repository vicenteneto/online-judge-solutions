# -*- coding: utf-8 -*-

cont = 0
for i in range(5):
    x = int(raw_input())
    if x % 2 == 0:
        cont += 1

print '%d valores pares' % cont
