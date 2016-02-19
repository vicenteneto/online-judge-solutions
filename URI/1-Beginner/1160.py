# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    pa, pb, g1, g2 = [float(x) for x in raw_input().split()]

    for j in range(1, 101):
        pa += int((pa * g1) / 100)
        pb += int((pb * g2) / 100)

        if pa > pb:
            print '%d anos.' % j
            break
        elif j == 100:
            print 'Mais de 1 seculo.'
