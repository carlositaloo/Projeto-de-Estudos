# 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

from os import system
system('cls')

nm = input('Digite o nome da pessoa: ').strip().upper().split()

# pm = nm.upper().split()
print('SILVA' in nm)
