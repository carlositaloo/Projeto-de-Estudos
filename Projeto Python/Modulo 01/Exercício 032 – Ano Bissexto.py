# 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from os import system
from rich import print
from datetime import date

system('cls')

ano = int(input('Digite um ano: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} É bissexto')
else:
    print(f'O ano de {ano} NÃO É bissexto')
print('\n\n\n')
