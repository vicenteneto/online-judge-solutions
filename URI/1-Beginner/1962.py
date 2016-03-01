# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    n = int(raw_input())

    print str(n - 2014) + ' A.C.' if n >= 2015 else str(2015 - n) + ' D.C.'
