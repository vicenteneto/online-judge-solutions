# -*- coding: utf-8 -*-

salary = float(raw_input())

if salary <= 400:
    increase = 15
elif salary <= 800:
    increase = 12
elif salary <= 1200:
    increase = 10
elif salary <= 2000:
    increase = 7
else:
    increase = 4

new_salary = salary + salary * (increase / 100.0)
print 'Novo salario: %.2f' % new_salary
print 'Reajuste ganho: %.2f' % (new_salary - salary)
print 'Em percentual: %d' % increase, '%'
