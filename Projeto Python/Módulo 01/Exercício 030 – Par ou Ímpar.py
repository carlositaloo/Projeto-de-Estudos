# 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from os import system
from rich import print

system('cls')

n1 = int(input('Digite um numero: '))

if n1 % 2 == 0:
	print('Seu numero é PAR')
else:
	print('Seu numero é IMPAR')