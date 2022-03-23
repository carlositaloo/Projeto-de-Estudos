# 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from os import system
from datetime import date

system('cls')

print('Digite o ano de nascimento de 7 pessoas:')
n1 = int()
n2 = int()
for c in range(0, 7):
	n = int(input(': '))
	a = date.today().year
	if a - n >= 18:
		n1 = n1 + 1
	elif a - n < 18:
		n2 = n2 + 1
	else:
		print('ERRO!')
print(f'{n1} pessoas são maior de 18\ne {n2} são menor de 18')