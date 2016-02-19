# -*- coding: utf-8 -*-

cont = 0
y = 0.5
for x in range(1, 40, 2):
    cont += float(x) / (y * 2)
    y *= 2

print '%.2f' % cont
