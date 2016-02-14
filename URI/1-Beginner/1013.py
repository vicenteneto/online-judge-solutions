# -*- coding: utf-8 -*-

def maior(a, b):
    return (a + b + abs(a - b)) / 2

a, b, c = [int(x) for x in raw_input().split()]
print '%d eh o maior' % (maior(maior(a, b), c))

