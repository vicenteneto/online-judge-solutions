# -*- coding: utf-8 -*-

a, b = [float(x) for x in raw_input().split()]

print '%.2f' % ((b / a - 1) * 100) + '%'
