# -*- coding: utf-8 -*-

for i in range(int(raw_input())):
    line = raw_input().split()

    if sum([int(x) for x in raw_input().split()]) % 2 == 0:
        print line[0] if line[1] == 'PAR' else line[2]
    else:
        print line[0] if line[1] == 'IMPAR' else line[2]
