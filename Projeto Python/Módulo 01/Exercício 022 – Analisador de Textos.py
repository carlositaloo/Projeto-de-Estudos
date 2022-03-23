# 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

from os import system

system('cls')

nc = str((input('Digite seu nome: \n'))).strip()
# qc = nc.replace(' ', '')
# pm = nc.split()

print('')
print(nc.upper())
print(nc.lower())
print('Seu nome tem {} caracteres' .format(len(nc) - nc.count(' ')))
print('O nome: {} tem {} letras'.format(pm[0], nc.find(' ')), end='\n\n\n')

# print('O nome: {} tem {} letras'.format(pm[0], (len(pm[0]))), end='\n\n\n')
