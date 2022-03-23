# 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

from os import system

system('cls')

print('Digite o peso de 5 pessoas:')
menor = 0
maior = 0

for c in range(0, 5):
    peso = float(input(': '))
    if c == 0:
        menor = peso
        maior = peso
    else:
        if peso <= menor:
            menor = peso
        if peso >= maior:
            maior = peso
print(f'O maior peso é: {maior}')
print(f'O menor peso é: {menor}')