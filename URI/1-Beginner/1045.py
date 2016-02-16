# -*- coding: utf-8 -*-

A = sorted([float(x) for x in raw_input().split()], reverse=True)

if A[0] >= A[1] + A[2]:
    print 'NAO FORMA TRIANGULO'
else:
    if A[0] ** 2 == A[1] ** 2 + A[2] ** 2:
        print 'TRIANGULO RETANGULO'
    if A[0] ** 2 > A[1] ** 2 + A[2] ** 2:
        print 'TRIANGULO OBTUSANGULO'
    if A[0] ** 2 < A[1] ** 2 + A[2] ** 2:
        print 'TRIANGULO ACUTANGULO'
    if A[0] == A[1] and A[0] == A[2]:
        print 'TRIANGULO EQUILATERO'
    elif A[0] == A[1] or A[1] == A[2] or A[0] == A[2]:
        print 'TRIANGULO ISOSCELES'
