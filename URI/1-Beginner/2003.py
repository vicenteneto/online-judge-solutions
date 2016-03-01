# -*- coding: utf-8 -*-

while 1:
    try:
        hour, minute = [int(x) for x in raw_input().split(':')]

        t = 8 * 60
        h = hour * 60 + minute + 60

        print 'Atraso maximo:', 0 if t >= h else h - t
    except EOFError:
        break
