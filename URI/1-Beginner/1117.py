# -*- coding: utf-8 -*-

s_1 = s_2 = -1

while 1:
    score = float(raw_input())

    if score < 0 or score > 10:
        print 'nota invalida'
    else:
        if s_1 < 0:
            s_1 = score
        else:
            s_2 = score
            break

print 'media = %.2f' % ((s_1 + s_2) / 2)
