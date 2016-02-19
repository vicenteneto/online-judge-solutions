# -*- coding: utf-8 -*-


def fat(x):
    if x == 1:
        return x
    else:
        return x * fat(x - 1)


print fat(int(raw_input()))
