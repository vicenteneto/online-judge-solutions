# -*- coding: utf-8 -*-
from math import sqrt

x1, y1 = [float(x) for x in raw_input().split()]
x2, y2 = [float(x) for x in raw_input().split()]
print '%.4f' % (sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

