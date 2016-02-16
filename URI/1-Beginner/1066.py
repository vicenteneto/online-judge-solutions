# -*- coding: utf-8 -*-

cont_even = 0
cont_positive = 0
cont_negative = 0
for i in range(5):
    x = int(raw_input())
    if x % 2 == 0:
        cont_even += 1
    if x > 0:
        cont_positive += 1
    elif x < 0:
        cont_negative += 1

print '%d valor(es) par(es)' % cont_even
print '%d valor(es) impar(es)' % (5 - cont_even)
print '%d valor(es) positivo(s)' % cont_positive
print '%d valor(es) negativo(s)' % cont_negative
