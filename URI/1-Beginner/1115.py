# -*- coding: utf-8 -*-

while 1:
    x, y = [int(x) for x in raw_input().split()]

    if not x or not y:
        break

    if x > 0:
        if y > 0:
            print 'primeiro'
        else:
            print 'quarto'
    else:
        if y > 0:
            print 'segundo'
        else:
            print 'terceiro'
