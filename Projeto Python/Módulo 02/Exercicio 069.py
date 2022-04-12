from os import system

system('cls')

novo = 'S'
msexo = fsexo = maiorid = 0
sexo = 'XY'

while novo == 'S':
    novo = 'XY'
    idade = int(input('Digite a idade da pessoas: '))
    if idade > 18:
        maiorid += 1
    while sexo not in 'MF':
        sexo = input('Digite o sexo da pessoa: [M/F] : ').strip().upper()[0]
    if sexo == 'M':
        msexo += 1
    if sexo == 'F' and idade < 20:
        fsexo += 1
    while novo not in 'SN':
        novo = input('Deseja cadastrar mais uma pessoa: [S/N] : ').strip().upper()[0]
    sexo = 'XY'
    print()

print(f'{maiorid} pessoas tem são maiores de idade')
print(f'{msexo} sexo masculino foram cadastrados')
print(f'{fsexo} Feminos tem menos de 20 anos\n\n')
