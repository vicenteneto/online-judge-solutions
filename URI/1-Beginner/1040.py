# -*- coding: utf-8 -*-

n1, n2, n3, n4 = [float(x) for x in raw_input().split()]
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print 'Media: %.1f' % media
if media < 5:
    print 'Aluno reprovado.'
elif media >= 7:
    print 'Aluno aprovado.'
else:
    exame = float(raw_input())
    print 'Aluno em exame.'
    print 'Nota do exame: %.1f' % exame
    media = (media + exame) / 2

    if media < 5:
        print 'Aluno reprovado.'
    else:
        print 'Aluno aprovado.'
    print 'Media final: %.1f' % media
