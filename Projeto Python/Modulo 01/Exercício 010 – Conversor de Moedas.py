# 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

import os
clear = lambda: os.system('cls')
clear()

n1 = float(input('Digite um valor em reais para converter para dólar: '))
print('o valor de R$:{:.2f} está valendo: $:{:.2f}' .format(n1, n1/5.14), end='\n\n\n')
