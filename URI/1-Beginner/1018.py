# -*- coding: utf-8 -*-

def calc(n, value):
    qnt = 0
    if n >= value:
        qnt = n / value
    print '%d nota(s) de R$ %d,00' % (qnt, value)
    return n - qnt * value

n = int(raw_input())

print n
n = calc(n, 100)
n = calc(n, 50)
n = calc(n, 20)
n = calc(n, 10)
n = calc(n, 5)
n = calc(n, 2)
n = calc(n, 1)

