# -*- coding: utf-8 -*-

begin_h, begin_m, end_h, end_m = [int(x) for x in raw_input().split()]

if end_h <= begin_h:
    if end_m <= begin_m:
        hours = end_h + 23 - begin_h
    else:
        hours = end_h + 24 - begin_h
else:
    if end_m <= begin_m:
        hours = end_h - begin_h - 1
    else:
        hours = end_h - begin_h

if end_m <= begin_m:
    minutes = 60 - (begin_m - end_m)
else:
    minutes = end_m - begin_m

if minutes == 60:
    minutes = 0
    hours += 1

print 'O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (hours, minutes)
