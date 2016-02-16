# -*- coding: utf-8 -*-

number = float(raw_input())

if number < 0 or number > 100:
    print 'Fora de intervalo'
elif number <= 25:
    print 'Intervalo [0,25]'
elif number <= 50:
    print 'Intervalo (25,50]'
elif number <= 75:
    print 'Intervalo (50,75]'
else:
    print 'Intervalo (75,100]'
