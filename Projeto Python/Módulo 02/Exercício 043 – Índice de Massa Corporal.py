# 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

from os import system

system('cls')

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / altura ** 2
print(f'\n Seus IMC é: {imc:.1f}\n')

if imc < 18.6:
    print(' Abaixo do peso')
elif imc < 25.1:
    print(' Peso ideal')
elif imc < 30.1:
    print(' Sobrepeso')
elif imc < 40.1:
    print(' Obesidade')
elif imc > 40:
    print(' Obesidade mórbida')
print('\n\n')