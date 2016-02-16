# -*- coding: utf-8 -*-


s_1 = raw_input()
s_2 = raw_input()
s_3 = raw_input()

if s_1 == 'vertebrado':
    if s_2 == 'ave':
        if s_3 == 'carnivoro':
            print 'aguia'
        else:
            print 'pomba'
    else:
        if s_3 == 'onivoro':
            print 'homem'
        else:
            print 'vaca'
else:
    if s_2 == 'inseto':
        if s_3 == 'hematofago':
            print 'pulga'
        else:
            print 'lagarta'
    else:
        if s_3 == 'hematofago':
            print 'sanguessuga'
        else:
            print 'minhoca'
