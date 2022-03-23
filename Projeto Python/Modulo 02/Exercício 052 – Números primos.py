# 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from os import system
from rich import print

system('cls')

q = 0
n1 = int(input('Digite um número: '))
for c in range(1, n1+1):
    if n1 % c != 0 or n1 % 1 != 0:
        print(c, end=' ')
    elif n1 % c == 0 and n1 % 1 == 0:
        print(f'[bold red]{c}', end=' ')
        q += 1
if q == 2:
	print(f'\nO número [bold red]{n1}[/bold red] é primo!\n')
else:
	print(f'\nO número {n1} NÃO é primo!\n')