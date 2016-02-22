# -*- coding: utf-8 -*-

while 1:
    n = int(raw_input())

    if not n:
        break

    A = [['1' for x in range(n)] for y in range(n)]
    last_len = len(str((2 ** (n - 1)) ** 2))

    for i in range(n):
        line = ''
        for j in range(n):
            if i == 0 and j == 0:
                A[i][j] = '1'
            elif j == 0:
                A[i][j] = str(int(A[i - 1][j]) * 2)
            elif j > 0:
                A[i][j] = str(int(A[i][j - 1]) * 2)

            actual_len = len(A[i][j])
            line += (last_len - actual_len) * ' ' + A[i][j] if actual_len < last_len else A[i][j]
            line += ' ' if j != n - 1 else ''

        print line
    print
