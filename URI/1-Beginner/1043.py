# -*- coding: utf-8 -*-

a, b, c = [float(x) for x in raw_input().split()]

if a + b > c and a + c > b and b + c > a:
    print 'Perimetro = %.1f' % (a + b + c)
else:
    print 'Area = %.1f' % (((a + b) * c) / 2)
