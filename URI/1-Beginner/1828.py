# -*- coding: utf-8 -*-

for i in range(1, int(raw_input()) + 1):
    sheldon, raj = [x for x in raw_input().split()]

    if sheldon == 'tesoura':
        if raj == 'papel' or raj == 'lagarto':
            message = 'Bazinga!'
        elif raj == 'Spock' or raj == 'pedra':
            message = 'Raj trapaceou!'
        else:
            message = 'De novo!'
    elif sheldon == 'papel':
        if raj == 'pedra' or raj == 'Spock':
            message = 'Bazinga!'
        elif raj == 'tesoura' or raj == 'lagarto':
            message = 'Raj trapaceou!'
        else:
            message = 'De novo!'
    elif sheldon == 'pedra':
        if raj == 'lagarto' or raj == 'tesoura':
            message = 'Bazinga!'
        elif raj == 'papel' or raj == 'Spock':
            message = 'Raj trapaceou!'
        else:
            message = 'De novo!'
    elif sheldon == 'lagarto':
        if raj == 'Spock' or raj == 'papel':
            message = 'Bazinga!'
        elif raj == 'pedra' or raj == 'tesoura':
            message = 'Raj trapaceou!'
        else:
            message = 'De novo!'
    else:
        if raj == 'tesoura' or raj == 'pedra':
            message = 'Bazinga!'
        elif raj == 'lagarto' or raj == 'papel':
            message = 'Raj trapaceou!'
        else:
            message = 'De novo!'

    print 'Caso #%d: %s' % (i, message)
