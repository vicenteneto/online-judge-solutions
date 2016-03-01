# -*- coding: utf-8 -*-

x = 1
while 1:
    try:
        n = int(raw_input())
        sequence = '0'

        for i in range(1, n + 1):
            for j in range(i):
                sequence += ' ' + str(i)

        print 'Caso %d: %d' % (x, len(sequence.split())), 'numero' if n == 0 else 'numeros'
        print sequence
        print

        x += 1
    except EOFError:
        break
