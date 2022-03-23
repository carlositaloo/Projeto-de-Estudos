# 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from os import system

system('cls')

for c in range(2, 51, 2):
    print(c, end=' ')
