# 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

from os import system

system('cls')

n = int(input('Digite a quantidade de sequencia de fibonacci: '))
F1 = 1
F2 = 1
Fn = 0

print()

while n > 0:
    print(f'{Fn}, ', end='')
    F1 = F2
    F2 = Fn
    Fn = F1 + F2
    n -= 1
print('\n\n')