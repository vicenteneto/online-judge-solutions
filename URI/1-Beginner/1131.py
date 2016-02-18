# -*- coding: utf-8 -*-


def recalculate():
    while 1:
        print 'Novo grenal (1-sim 2-nao)'
        res = int(raw_input())

        if res == 1:
            return True
        elif res == 2:
            return False


cont = inter = gremio = 0

while 1:
    x, y = [int(x) for x in raw_input().split()]

    if x > y:
        inter += 1
    elif x < y:
        gremio += 1

    cont += 1

    if not recalculate():
        break

print '%d grenais' % cont
print 'Inter:%d' % inter
print 'Gremio:%d' % gremio
print 'Empates:%d' % (cont - inter - gremio)
if inter > gremio:
    print 'Inter venceu mais'
elif gremio > inter:
    print 'Gremio venceu mais'
else:
    print 'Nao houve vencedor'
