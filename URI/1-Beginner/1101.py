# -*- coding: utf-8 -*-

while 1:
    m, n = [int(x) for x in raw_input().split()]

    if m <= 0 or n <= 0:
        break

    if m > n:
        m, n = n, m

    count = 0
    for i in range(m, n + 1):
        count += i
        print i,

    print 'Sum=%d' % count
