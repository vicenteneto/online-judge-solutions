# -*- coding: utf-8 -*-

par = []
impar = []

for i in range(15):
    x = int(raw_input())

    if x % 2 == 0:
        par += [x]
    else:
        impar += [x]

    if len(impar) == 5:
        for j in range(5):
            print 'impar[%d] = %d' % (j, impar[j])
        impar = []

    if len(par) == 5:
        for j in range(5):
            print 'par[%d] = %d' % (j, par[j])
        par = []

for j in range(len(impar)):
    print 'impar[%d] = %d' % (j, impar[j])

for j in range(len(par)):
    print 'par[%d] = %d' % (j, par[j])
