# -*- coding: utf-8 -*-

x = y = z = int(raw_input())

while z <= x:
    z = int(raw_input())

cont = x
while 1:
    y += 1

    cont += y
    if cont > z:
        break

print y - x + 1
