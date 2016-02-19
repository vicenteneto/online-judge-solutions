# -*- coding: utf-8 -*-

t = int(raw_input())

u = 0
for i in range(1000):
    print 'N[%d] = %d' % (i, u)
    u = 0 if u == t - 1 else u + 1
