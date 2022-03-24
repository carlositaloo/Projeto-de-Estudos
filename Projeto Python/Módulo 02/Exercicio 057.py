from os import system

system('cls')

sexo = input('Digite o sexo da pessoa [F/M]: ').upper()

while sexo not in 'MF':
    sexo = input('Você digitou errado, digite novamente [F/M]: ').upper()
if sexo == 'M':
    sexo = 'Masculino'
if sexo == 'F':
    sexo = 'Feminino'
print(f'\nO sexo digitado é: {sexo}\n')