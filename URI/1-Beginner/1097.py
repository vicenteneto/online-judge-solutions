# -*- coding: utf-8 -*-

j = 7

for i in range(1, 10, 2):
    print 'I=%d J=%d' % (i, j)
    print 'I=%d J=%d' % (i, j - 1)
    print 'I=%d J=%d' % (i, j - 2)
    j += 2
