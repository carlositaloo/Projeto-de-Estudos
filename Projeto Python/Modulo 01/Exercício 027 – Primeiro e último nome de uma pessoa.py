# 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

from os import system
system('cls')

nc = input('Digite seu nome completo: ')
nl = nc.split()
# un = nc.count(' ')

print('')
print('Primeiro nome: {}' .format(nl[0].title()))
print('último nome: {}' .format(nl[len(nl)-1].title()), end='\n\n\n')
# print('último nome: {}' .format(nl[un].title()), end='\n\n\n')
