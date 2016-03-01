# -*- coding: utf-8 -*-

students = []
notes = []

for i in range(int(raw_input())):
    line = raw_input().split()
    students += [int(line[0])]
    notes += [float(line[1])]

max_index = notes.index(max(notes))
print 'Minimum note not reached' if notes[max_index] < 8 else students[max_index]
