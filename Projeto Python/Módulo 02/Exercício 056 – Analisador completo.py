# 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from os import system

system('cls')

print('Registro de 4 pessoas:')
maior = int()
menor = int()
media = int()

for c in range(0, 4):
    print(f'--- {c+1}ª Pessoa ---')
    nome = input('Nome: ').title().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper()

    media = idade + media
    if sexo == 'M' and idade > maior:
        maior = idade
        masculino = nome
    if sexo == 'F' and idade < 20:

        menor = menor + 1

print(f'A média de idade é: {media / 4}')
print(f'O nome do homem mais velhor é: {masculino} com {maior} anos')
print(f'{menor} Femininos sao menores de idade')
