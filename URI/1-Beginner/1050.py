# -*- coding: utf-8 -*-

ddd = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro', 32: 'Juiz de Fora', 19: 'Campinas',
       27: 'Vitoria', 31: 'Belo Horizonte'}

key = int(raw_input())
if key in ddd.keys():
    print ddd[key]
else:
    print 'DDD nao cadastrado'
