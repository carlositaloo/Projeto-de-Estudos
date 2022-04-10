# 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

from os import system

system('cls')

sexo = input('Digite o sexo da pessoa [F/M]: ').upper().strip()[0]

while sexo not in 'MF':
    sexo = input('Você digitou errado, digite novamente [F/M]: ').upper().strip()[0]
if sexo == 'M':
    sexo = 'Masculino'
if sexo == 'F':
    sexo = 'Feminino'
print(f'\nO sexo digitado é: {sexo}\n')