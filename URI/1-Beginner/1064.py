# -*- coding: utf-8 -*-

A = [float(raw_input()) for i in range(6)]
cont = sum([1 for x in A if x > 0])
soma = sum([x for x in A if x > 0])

print '%d valores positivos' % cont
print '%.1f' % (soma / float(cont))
