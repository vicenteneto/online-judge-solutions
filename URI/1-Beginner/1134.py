# -*- coding: utf-8 -*-

fuel = {1: 0, 2: 0, 3: 0}

while 1:
    fuel_type = int(raw_input())

    if fuel_type == 1:
        fuel[1] += 1
    elif fuel_type == 2:
        fuel[2] += 1
    elif fuel_type == 3:
        fuel[3] += 1
    elif fuel_type == 4:
        break

print 'MUITO OBRIGADO'
print 'Alcool: %d' % fuel[1]
print 'Gasolina: %d' % fuel[2]
print 'Diesel: %d' % fuel[3]
