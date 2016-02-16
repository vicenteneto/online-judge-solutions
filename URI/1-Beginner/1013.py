# -*- coding: utf-8 -*-


def maior(number_a, number_b):
    return (number_a + number_b + abs(number_a - number_b)) / 2


a, b, c = [int(x) for x in raw_input().split()]
print '%d eh o maior' % (maior(maior(a, b), c))
