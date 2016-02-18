# -*- coding: utf-8 -*-

while 1:
    x, y = [int(x) for x in raw_input().split()]

    if x == y:
        break

    if x > y:
        print 'Decrescente'
    else:
        print 'Crescente'
