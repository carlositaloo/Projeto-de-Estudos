# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

from os import system

system('cls')

tupla = ('Notebook', 7500.80,
         'Tablet', 3000,
         'Mouse', 450,
         'Teclado', 700.90,
         'Headset', 350,
         'Internet', 70.50)

print('+-' * 16)
print(f'{"LISTA DE PREÇOS":^31}')

for c in range(0, len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:.<20}', end='')
    else:
        print(f'R$:{tupla[c]:>8.2f}')
print('+-' * 16)
print('')
