# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    x = int(raw_input())

    prime = True
    if x % 2 == 0:
        prime = False
    else:
        for j in range(3, int(x / 2) + 2, 2):
            if x % j == 0:
                prime = False
                break

    print x, 'eh primo' if prime else 'nao eh primo'
