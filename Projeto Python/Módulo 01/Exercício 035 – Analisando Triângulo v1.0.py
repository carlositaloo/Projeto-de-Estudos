# 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from os import system
from rich import print

system('cls')

n1 = input('Primeira medida: ')
n2 = input(' Segunda medida: ')
n3 = input('Terceira medida: ')

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('As medidas colocadas da para fazer um triangulo!')
else:
    print('As medida dadas nao compoem um triangulo!')
print('\n\n\n')
