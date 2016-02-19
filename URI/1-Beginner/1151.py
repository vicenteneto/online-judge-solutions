# -*- coding: utf-8 -*-


def fibonacci(x, a=0, b=1, sequence='0 1'):
    if x == 1:
        return '0'
    if x == 2:
        return sequence
    else:
        sequence += ' %d' % (a + b)
        return fibonacci(x - 1, b, a + b, sequence)

print fibonacci(int(raw_input()))
