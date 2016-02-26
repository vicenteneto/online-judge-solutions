# -*- coding: utf-8 -*-

while 1:
    try:
        n = int(raw_input())

        A = [[0 for x in range(n)] for y in range(n)]

        y = n - 1
        for x in range(n):
            A[x][x] = 2
            A[x][y] = 3
            y -= 1

        start = n / 3
        for x in range(start, n - start):
            for y in range(start, n - start):
                A[x][y] = 1

        A[n / 2][n / 2] = 4

        for x in range(n):
            line = ''
            for y in range(n):
                line += str(A[x][y])
            print line
        print
    except EOFError:
        break
