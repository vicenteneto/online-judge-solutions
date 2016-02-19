# -*- coding: utf-8 -*-


def fib(v, a=0, b=1):
    if v == 0:
        return a
    elif v == 1:
        return b
    else:
        return fib(v-1, b, a + b)

for i in range(int(raw_input())):
    n = int(raw_input())
    print 'Fib(%.0f) = %d' % (n, fib(n))
