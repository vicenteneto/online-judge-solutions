# -*- coding: utf-8 -*-

characters = {'C': 0, 'R': 0, 'S': 0}

for i in range(int(raw_input())):
    amount, c_type = [x for x in raw_input().split()]
    characters[c_type] += int(amount)

total = characters['C'] + characters['R'] + characters['S']

print 'Total: %d cobaias' % total
print 'Total de coelhos: %d' % characters['C']
print 'Total de ratos: %d' % characters['R']
print 'Total de sapos: %d' % characters['S']
print 'Percentual de coelhos: %.2f' % (characters['C'] * 100.0 / total), '%'
print 'Percentual de ratos: %.2f' % (characters['R'] * 100.0 / total), '%'
print 'Percentual de sapos: %.2f' % (characters['S'] * 100.0 / total), '%'
