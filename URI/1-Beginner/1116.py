# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    x, y = [float(x) for x in raw_input().split()]

    if not y:
        print 'divisao impossivel'
    else:
        print '%.1f' % (x / y)
