# -*- coding: utf-8 -*-

x = float(raw_input())

for i in range(100):
    print 'N[%d] = %.4f' % (i, x)
    x /= 2
