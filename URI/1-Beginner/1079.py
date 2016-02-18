# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    a, b, c = [float(x) for x in raw_input().split()]
    print '%.1f' % ((a * 2 + b * 3 + c * 5) / 10)
