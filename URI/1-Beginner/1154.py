# -*- coding: utf-8 -*-

ages = []

while 1:
    age = float(raw_input())
    if age >= 0:
        ages += [age]
    else:
        break

print '%.2f' % (sum([x for x in ages]) / len(ages))
