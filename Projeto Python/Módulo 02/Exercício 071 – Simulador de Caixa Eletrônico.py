# 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from os import system

system('cls')

sacar = int(input('Valor a sacar R$: '.rjust(28)))
cedulas = (200, 100, 50, 20, 10, 5, 1)
c = 0
print('-='*20, end='-\n')

while sacar > 0:
    quantidade = sacar // cedulas[c]
    sacar -= quantidade * cedulas[c]
    if quantidade > 0:
        print(f'{quantidade:3} cédulas de R$: {cedulas[c]:3}'.center(40))
    c += 1
print('-='*20, end='-\n\n')

