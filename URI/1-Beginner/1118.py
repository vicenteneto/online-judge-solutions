# -*- coding: utf-8 -*-


def recalculate():
    while 1:
        print 'novo calculo (1-sim 2-nao)'
        res = int(raw_input())
        if res == 1:
            return True
        elif res == 2:
            return False


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
            print 'media = %.2f' % ((s_1 + s_2) / 2)
            if recalculate():
                s_1 = s_2 = -1
            else:
                break
