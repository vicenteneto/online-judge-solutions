# -*- coding: utf-8 -*-

prices = {1001: 1.5, 1002: 2.5, 1003: 3.5, 1004: 4.5, 1005: 5.5}
total = 0.0

for i in range(int(raw_input())):
    product, quantity = [int(x) for x in raw_input().split()]

    total += prices[product] * quantity

print '%.2f' % total
