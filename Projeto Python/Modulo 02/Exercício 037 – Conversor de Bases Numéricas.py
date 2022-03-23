# 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from os import system
system('cls')

n1 = int(input('Digite um numero para convertê-lo: '))
op = int(input('Digite o numero de uma das opções:\n    1. Binário\n    2. Octal\n    3. Hexadecimal\nOpção: '))

if op == 1:
    print(f'O valor {n1} em Binário é: {bin(n1)[2:]}')
elif op == 2:
    print(f'O valor {n1} em Octal é: {oct(n1)[2:]}')
elif op == 3:
    print(f'O valor {n1} em Hexadecimal é: {hex(n1)[2:]}')
else:
    print('Voce escolheu uma opção invalida!')
