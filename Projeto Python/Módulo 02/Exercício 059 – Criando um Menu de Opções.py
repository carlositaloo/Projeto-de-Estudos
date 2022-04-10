# 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from os import system

system('cls')

print('Digite 2 valores: ')
n1 = int(input(': '))
n2 = int(input(': '))
sair = 0
while sair != 1:
    print(f'Números digitados: {n1} e {n2}')
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos numeros')
    print('[0] - Sair')
    menu = int(input('Opção: '))
    
    if menu == 1:
        print(f'\nA soma dos 2 numero é: {n1}+{n2}={n1+n2}\n\n')
    elif menu == 2:
        print(f'\nA multiplicação dos números é: {n1}x{n2}={n1*n2}\n\n')
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\nO maior valor é: {maior}\n\n')
    elif menu == 4:
        print('\nDigite 2 valores: ')
        n1 = int(input(': '))
        n2 = int(input(': '))
    elif menu == 0:
        sair = 1
    else:
        print('\nOpção invalida!')
        menu = int(input('Opção: '))
