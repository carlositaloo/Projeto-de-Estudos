# 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

from os import system

system('cls')

msexo = fsexo = maiorid = 0
sexo = ' '

while True:
    idade = int(input('Digite a idade da pessoas: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo da pessoa: [M/F] : ').strip().upper()[0]
    if idade > 18:
        maiorid += 1
    if sexo == 'M':
        msexo += 1
    if sexo == 'F' and idade < 20:
        fsexo += 12
    sair = ' '
    while sair not in 'SN':
        sair = input('Deseja cadastrar mais uma pessoa: [S/N] : ').strip().upper()[0]
    if sair == 'N':
        break
    print()

print(f'\n{maiorid} pessoas são maiores de idade')
print(f'{msexo} sexo masculino foram cadastrados')
print(f'{fsexo} Feminos tem menos de 20 anos\n\n')
