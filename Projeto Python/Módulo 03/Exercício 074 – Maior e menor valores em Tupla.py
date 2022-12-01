# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from os import system
from random import randint


system('cls')

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('\nNúmeros randomizados:\n', tupla)

print(f'\nO maior numero da tupla é: {max(tupla)}')
print(f'O menor numero da tupla é: {min(tupla)}\n\n')

# max = tupla[0]
# for c in range(0, 5):
#     if max <= tupla[c]:
#         max = tupla[c]
# print(f'O maior numero da tupla é: {max}')

# min = tupla[0]
# for c in range(0, 5):
#     if min >= tupla[c]:
#         min = tupla[c]
# print(f'O menor numero da tupla é: {min}')
# print('\n\n')