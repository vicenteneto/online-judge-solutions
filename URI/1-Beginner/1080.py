# -*- coding: utf-8 -*-

higher = position = -1

for i in range(1, 101):
    x = int(raw_input())
    if x > higher:
        higher, position = x, i

print higher
print position
