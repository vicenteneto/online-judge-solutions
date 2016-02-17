# -*- coding: utf-8 -*-

n = int(raw_input())

for i in range(n):
    x = int(raw_input())
    if x == 0:
        print 'NULL'
    elif x < 0:
        if x % 2 == 0:
            print 'EVEN NEGATIVE'
        else:
            print 'ODD NEGATIVE'
    else:
        if x % 2 == 0:
            print 'EVEN POSITIVE'
        else:
            print 'ODD POSITIVE'
