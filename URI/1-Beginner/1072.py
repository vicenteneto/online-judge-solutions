# -*- coding: utf-8 -*-

n = int(raw_input())
A = [int(raw_input()) for i in range(n)]

in_count = sum([1 for i in A if i in range(10, 21)])
print '%d in' % in_count
print '%d out' % (n - in_count)
