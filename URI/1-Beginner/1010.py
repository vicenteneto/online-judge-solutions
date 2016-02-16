# -*- coding: utf-8 -*-

cod_1, qnt_1, price_1 = [x for x in raw_input().split()]
cod_2, qnt_2, price_2 = [x for x in raw_input().split()]
print 'VALOR A PAGAR: R$ %.2f' % (int(qnt_1) * float(price_1) + int(qnt_2) * float(price_2))
