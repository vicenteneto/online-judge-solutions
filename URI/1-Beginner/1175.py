# -*- coding: utf-8 -*-

A = list(reversed([int(raw_input()) for i in range(20)]))

for i in range(20):
    print 'N[%d] = %d' % (i, A[i])
