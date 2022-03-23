# 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

import os
clear = lambda: os.system('cls')
clear()

n1 = float(input('Digite o valor do produto pra saber quanto ficara com desconto de 5%: '))
n2 = (n1 / 100) * 5
# n2 = n1*5/100
print('O valor do produto ficara: R$:{:.2f}' .format(n1 - n2))
