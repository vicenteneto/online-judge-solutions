# -*- coding: utf-8 -*-

try:
    while 1:
        n = int(raw_input())

        A = [[3 for i in range(n)] for j in range(n)]

        x = n - 1
        for i in range(n):
            A[i][i] = 1
            A[i][x] = 2
            x -= 1

        for i in range(n):
            line = ''
            for j in range(n):
                line += str(A[i][j])
            print line

except EOFError:
    pass
