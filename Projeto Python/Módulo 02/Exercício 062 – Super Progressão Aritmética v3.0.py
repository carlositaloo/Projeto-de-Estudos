# 062: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

from os import system

system('cls')

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
res = p
sair = 1
count = 10

while c < 10:
    print(f'{res} ➜  ', end='')
    res += r
    c += 1

while sair != 0:
    sair = int(input('\nQuer ver mais quantas quantia da mesma PA: '))
    count += sair
    c = 0
    res = p
    system('cls')
    while c < count:
        print(f'{res} ➜  ', end='')
        res += r
        c += 1
    print()
