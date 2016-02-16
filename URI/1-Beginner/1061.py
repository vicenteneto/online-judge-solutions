# -*- coding: utf-8 -*-

begin_d = int(raw_input().split('Dia ')[1])
begin_h, begin_m, begin_s = [int(x) for x in raw_input().split(' : ')]
end_d = int(raw_input().split('Dia ')[1])
end_h, end_m, end_s = [int(x) for x in raw_input().split(' : ')]

seconds = 0
minutes = 0
hours = 0
days = 0

if end_d == begin_d:
    days = 0
else:
    days = end_d - begin_d
    if end_h < begin_h or end_m < begin_m or end_s < begin_s:
        days -= 1

if end_h == begin_h:
    hours = 0
else:
    hours = end_h - begin_h
    if end_m < begin_m or end_s < end_s:
        hours -= 1
    if hours < 0:
        hours += 24

if end_m == begin_m:
    minutes = 0
else:
    minutes = end_m - begin_m
    if end_s < begin_s:
        minutes -= 1
    if minutes < 0:
        minutes += 60

if end_s == begin_s:
    seconds = 0
else:
    seconds = end_s - begin_s
    if seconds < 0:
        seconds += 60

print '%d dia(s)' % days
print '%d hora(s)' % hours
print '%d minuto(s)' % minutes
print '%d segundo(s)' % seconds
