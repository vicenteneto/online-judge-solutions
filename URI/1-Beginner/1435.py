# -*- coding: utf-8 -*-

while 1:
    n = int(raw_input())

    if not n:
        break

    K = [min(i, n - 1 - i) + 1 for i in range(n)]
    S = [[str(min(K[i], K[j])) for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if j == n - 1:
                if len(S[i][j]) == 1:
                    print "  " + S[i][j]
                elif len(S[i][j]) == 2:
                    print " " + S[i][j]
                else:
                    print S[i][j]
            else:
                if len(S[i][j]) == 1:
                    print "  " + S[i][j],
                elif len(S[i][j]) == 2:
                    print " " + S[i][j],
                else:
                    print S[i][j],

    print
