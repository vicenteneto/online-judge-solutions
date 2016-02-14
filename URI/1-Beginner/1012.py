# -*- coding: utf-8 -*-

a, b, c = [float(x) for x in raw_input().split()]
print 'TRIANGULO: %.3f' % (a * c / 2)
print 'CIRCULO: %.3f' % (3.14159 * c * c)
print 'TRAPEZIO: %.3f' % ((a + b) * c / 2)
print 'QUADRADO: %.3f' % (b * b)
print 'RETANGULO: %.3f' % (a * b)

