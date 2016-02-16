# -*- coding: utf-8 -*-

salary = float(raw_input())

if salary <= 2000:
    print 'Isento'
else:
    if salary <= 3000:
        taxes = (salary - 2000) * 0.08
    elif salary <= 4500:
        taxes = 1000 * 0.08 + (salary - 3000) * 0.18
    else:
        taxes = 1000 * 0.08 + 1500 * 0.18 + (salary - 4500) * 0.28

    print 'R$ %.2f' % taxes
