# 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

import os
clear = lambda: os.system('cls')
clear()

d = int(input('Por quantos dias o carro ficou alugado: '))
km = float(input('Quantos KMs foram percorrido com o carro: '))

km = km * 0.15
d = d * 60

print('\nO valor do aluguel ficou: R$:{:.2f}' .format(km + d), end='\n\n\n')