# -*- coding: utf-8 -*-

for i in range(1, int(raw_input()) * 4, 4):
    sequence = ''
    for j in range(i, i + 3):
        sequence += '%d ' % j
    print sequence + 'PUM'
