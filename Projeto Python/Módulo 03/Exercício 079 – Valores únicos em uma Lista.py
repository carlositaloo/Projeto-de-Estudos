# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

from os import system
from random import randint

system('cls')
lista = []

randomizar = input('Deseja randomizar? [S/N]: ').upper()

# if randomizar == 'N':
#     while True:
#         v = int(input('Digite um número: '))
#         if v not in lista:
#             lista.append(v)
#         else:
#             print('Esse numero já existe. ', end='')
#         fim = input('Deseja sair? [S/N]: ')
#         if fim in 'Nn':
#             break
#     print(f'\n\nLista feita:\n{lista}\n\nLista organizada:\n{sorted(lista)}\n\n')

if randomizar == 'N':
    while True:
        v = int(input('Digite um número: '))
        if v in lista:
            print('Esse numero já existe. ', end='')
        else:
            lista.append(v)
        fim = input('Deseja continuar? [S/N]: ').upper()
        if fim == 'N':
            break
    print(f'\n\nLista feita:\n{lista}\n\nLista organizada:\n{sorted(lista)}\n\n')

if randomizar == 'S':
    while True:
        cont = randint(3, 10)
        for c in range(cont):
            print("Digite um número: ", end='')
            v = randint(1, 10)
            print(v)
            lista.append(v)
        break
    print(f'\n\nLista feita:\n{lista}\n\nLista organizada:\n{sorted(lista)}\n\n')