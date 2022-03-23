# 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

from os import system

system('cls')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O {n1} é maior que o {n2}\n\n')
elif n2 > n1:
    print(f'O {n2} é maior que o {n1}\n\n')
else:
    print(f'O dois número: {n1} e {n2} são o mesmo!\n\n')
