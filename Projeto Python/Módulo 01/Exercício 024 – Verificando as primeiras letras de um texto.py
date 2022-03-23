# 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

from os import system
system('cls')

nm = input('Digite o nome da cidade: ').strip()

print(nm[:5].upper() == 'SANTO')

# pm = nm.upper().split()
# print('SANTO' in pm[0])
