# 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from os import system
system('cls')

print('Simular empréstimo para compra de imóvel:')
valorcasa = float(input('Digite o valor da Casa: '))
salario = float(input('Digite o valor do seu salario: '))
meses = int(input('Em quanto meses deseja parcelar: '))

parcela = float(valorcasa / meses)
trinta = float(salario * 30 / 100)

if trinta >= parcela:
    print(f'\n  Você conseguiu o empréstimo\n\n    A parcela ficara: {parcela:.2f}\n    E 30% do seu salario é: {trinta:.2f}\n    Parcelamento ficou em : {meses / 12:.0f} anos\n\n\n')
else:
    print(f'\n  Infelizmente não foi possível efetuar o empréstimo!\n\n    O valor da parcela é {parcela:.2f}\n    E 30% do seu salario é: {trinta:.2f}\n    Parcelado em : {meses / 12:.0f} anos\n\n\n')

