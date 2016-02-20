# -*- coding: utf-8 -*-

raw_input()
A = [int(x) for x in raw_input().split()]

minimum = min(A)
print 'Menor valor:', minimum
print 'Posicao:', A.index(minimum)
