# -*- coding: utf-8 -*-

while 1:
    try:
        raw_input()
        faster = max([int(x) for x in raw_input().split()])

        print 1 if faster < 10 else 2 if faster < 20 else 3
    except EOFError:
        break
