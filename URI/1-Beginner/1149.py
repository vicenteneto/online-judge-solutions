# -*- coding: utf-8 -*-

A = [int(x) for x in raw_input().split()]

n = next(A[i] for i in range(1, len(A)) if A[i] > 0)

print sum([x for x in range(A[0], A[0] + n)])
