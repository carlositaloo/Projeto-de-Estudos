# 061: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

from os import system

system('cls')

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
t = p

while c < 10:
    print(f'{t} ➜  ', end='')
    t += r
    c += 1