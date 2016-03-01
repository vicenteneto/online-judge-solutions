# -*- coding: utf-8 -*-

p, n = [int(x) for x in raw_input().split()]
pipes = [int(x) for x in raw_input().split()]

last = pipes[0]
game_over = False

for height in pipes:
    if height > last + p or height < last - p:
        game_over = True
        break
    last = height

print 'GAME OVER' if game_over else 'YOU WIN'
