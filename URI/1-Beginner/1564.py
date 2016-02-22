# -*- coding: utf-8 -*-

try:
    while 1:
        n = int(raw_input())

        if n:
            print 'vai ter duas!'
        else:
            print 'vai ter copa!'
except EOFError:
    pass
