# -*- coding: utf-8 -*-

raw_input()
A = [int(x) for x in raw_input().split()]

print A.index(min(A)) + 1
