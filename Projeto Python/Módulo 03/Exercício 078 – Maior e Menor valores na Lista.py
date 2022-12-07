# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

from os import system
from random import randint

system('cls')

lista = []
for c in range(5):
    # lista.append(randint(1, 99))
    lista.append(int(input(f'Digite um numero {c+1}ª:')))
print(f'\n{lista}\n')

posmin = ''
posmax = ''

for p, v in enumerate(lista):
    if v == min(lista):
        posmin += (f'{p+1}ª, ')
    if v == max(lista):
        posmax += (f'{p+1}ª, ')
print(f'O menor valor da lista é: {min(lista)} na {posmin} posição')
print(f'O maior valor da lista é: {max(lista)} na {posmax} posição\n\n')

# valormin = lista[0]
# for p, v in enumerate(lista):
#     if valormin >= v:
#         valormin = v
#         pmin = p
# valormax = lista[0]
# for p, v in enumerate(lista):
#     if valormax <= v:
#         valormax = v
#         pmax = p

# print(f'\nValor minimo é: {valormin} na {pmin+1}ª posição.')
# print(f'Valor maixmo é: {valormax} na {pmax+1}ª posição.\n\n')

