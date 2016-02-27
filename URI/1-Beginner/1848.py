# -*- coding: utf-8 -*-

cont = 0
while 1:
    try:
        line = raw_input()

        if len(line.split()) == 2:
            print cont
            cont = 0
        else:
            if line[0] == '*':
                cont += 4
            if line[1] == '*':
                cont += 2
            if line[2] == '*':
                cont += 1
    except EOFError:
        break
