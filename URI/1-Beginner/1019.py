# -*- coding: utf-8 -*-

n = int(raw_input())
hours = int(n / 3600)
n -= hours * 3600
minutes = int(n / 60)
n -= minutes * 60
print '%d:%d:%d' % (hours, minutes, n)
