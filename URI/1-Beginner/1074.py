# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
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
