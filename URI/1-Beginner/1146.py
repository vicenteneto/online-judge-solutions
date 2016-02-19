# -*- coding: utf-8 -*-

while 1:
    x = int(raw_input())

    if not x:
        break

    sequence = ''
    for i in range(1, x + 1):
        sequence += '%d ' % i

    print sequence[:-1]
