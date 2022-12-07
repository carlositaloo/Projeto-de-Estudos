# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

from os import system

system('cls')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

list = (n1, n2, n3, n4)
tupla = (list)
pares = 0

print(f'\n{tupla}\n')

print(f'A tupla tem {tupla.count(9)} números 9.')

if 3 in tupla:
    print(f'A tupla tem o valor 3 na posição: {tupla.index(3)+1}ª')
else:
    print('A tupla não tem o número 3.')

for c in range(len(tupla)):
    if tupla[c] % 2 == 0:
        pares += 1

print(f'Os valores pares digitado foram: {pares}\nQue são eles: ', end='')

# for posicao, valor in enumerate(tupla):
#     if valor % 2 == 0:
#         print(valor, end=', ')

for c in tupla:
    if c % 2 == 0:
        print(c, end=', ')

print('\n\n')
