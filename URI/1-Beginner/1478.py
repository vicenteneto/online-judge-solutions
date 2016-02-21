# -*- coding: utf-8 -*-

while 1:
    n = int(raw_input())

    if not n:
        break

    M = [[1 for i in range(n)] for j in range(n)]
    S = [["" for i in range(n)] for j in range(n)]

    for i in range(n):
        if i != 0:
            k = M[i - 1][0] + 1
            asc = False
        else:
            k = 1
            asc = True

        for j in range(n):
            M[i][j] = k
            S[i][j] = str(M[i][j])
            if asc:
                k += 1
                if k == n + 1:
                    k -= 2
                    asc = False
            else:
                k -= 1
                if k == 0:
                    k += 2
                    asc = True

    for i in range(n):
        for j in range(n):
            if j != n - 1:
                if len(S[i][j]) == 1:
                    print "  " + S[i][j],
                elif len(S[i][j]) == 2:
                    print " " + S[i][j],
                else:
                    print S[i][j],
            else:
                if len(S[i][j]) == 1:
                    print "  " + S[i][j]
                elif len(S[i][j]) == 2:
                    print " " + S[i][j]
                else:
                    print S[i][j]
    print
