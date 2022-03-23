# 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from os import system
from rich import print

system('cls')

km = float(input('Digite a Distancia em KM: '))

if km <= 200:
	rs = km * 0.50
else:
	rs = km * 0.45
print(f'A passagem da viagem é R$:{rs:.2f}')
