# -*- coding: utf-8 -*-

age = int(raw_input())
years = int(age / 365)
age -= years * 365
months = int(age / 30)
age -= months * 30
print '%d ano(s)' % years
print '%d mes(es)' % months
print '%d dia(s)' % age
