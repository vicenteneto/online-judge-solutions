# -*- coding: utf-8 -*-

prices = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

product, quantity = [int(x) for x in raw_input().split()]

print 'Total: R$ %.2f' % (prices[product] * quantity)
