# -*- coding: utf-8 -*-

a, b = [int(x) for x in raw_input().split()]

if b % a == 0 or a % b == 0:
    print 'Sao Multiplos'
else:
    print 'Nao sao Multiplos'
