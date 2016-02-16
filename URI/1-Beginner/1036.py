# -*- coding: utf-8 -*-
from math import sqrt

a, b, c = [float(x) for x in raw_input().split()]
delta = (b ** 2) - 4 * a * c

if not a or delta < 0:
    print 'Impossivel calcular'
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    print 'R1 = %.5f' % x1
    print 'R2 = %.5f' % x2
