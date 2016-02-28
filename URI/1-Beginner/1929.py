# -*- coding: utf-8 -*-

A = [int(i) for i in raw_input().split()]
A.sort()

print 'S' if A[2] < A[0] + A[1] or A[3] < A[1] + A[2] else 'N'
