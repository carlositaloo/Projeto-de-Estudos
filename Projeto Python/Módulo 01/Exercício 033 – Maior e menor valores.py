# 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from os import system
from rich import print

system('cls')

print('Digite 3 numeros:')
n1 = int(input())
n2 = int(input())
n3 = int(input())

max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3

min = n1
if n2 < min:
    min = n2
if n3 < min:
    min = n3

print(f'O MAIOR numero é: {max}')
print(f'O MENOR numero é: {min}')
