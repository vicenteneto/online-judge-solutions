# -*- coding: utf-8 -*-

a, b, c = [int(x) for x in raw_input().split()]

if a < b:
    if b >= c:
        print ':('
    elif b < c:
        if c - b < b - a:
            print ':('
        else:
            print ':)'
    else:
        print ':('
elif a > b:
    if b <= c:
        print ':)'
    elif b > c:
        if c - b > b - a:
            print ':)'
        else:
            print ':('
elif a == b and b < c:
    print ':)'
else:
    print ':('
