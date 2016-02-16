# -*- coding: utf-8 -*-

begin, end = [int(x) for x in raw_input().split()]

if end <= begin:
    end += 24

print 'O JOGO DUROU %d HORA(S)' % (end - begin)
