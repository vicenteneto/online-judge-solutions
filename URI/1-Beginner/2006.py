# -*- coding: utf-8 -*-

t = int(raw_input())
print sum([1 for x in raw_input().split() if int(x) == t])
