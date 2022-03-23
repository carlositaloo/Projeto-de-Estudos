# 028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from os import system
from rich import print
from random import randint

system('cls')

n1 = randint(0, 5)
# print(f'{n1}')

n2 = int(input(('Digite um numero de 0 a 5 para saber se o numero foi acertado: ')))

if n1 == n2:
	print('Parabéns você acertou o numero da maquina!')
else:
	print('Que pena voce errou!')

