# -*- coding: utf-8 -*-


def formatted(f):
    return format(f, '.1f').rstrip('0').rstrip('.')


i, j = 0.0, 1.0
for k in range(0, 11):
    print 'I=' + formatted(i), 'J=' + formatted(j)
    print 'I=' + formatted(i), 'J=' + formatted(j + 1)
    print 'I=' + formatted(i), 'J=' + formatted(j + 2)
    i += 0.2
    j += 0.2
