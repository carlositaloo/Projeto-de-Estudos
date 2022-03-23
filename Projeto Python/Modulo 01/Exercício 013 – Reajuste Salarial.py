# 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

import os
clear = lambda: os.system('cls')
clear()

n1 = float(input('Digite o salario que ira ganhar 15%: '))
n2 = (n1 / 100) * 15

print(' O salario vai receber R$:{:.2f} de aumento.\n O salario atual: R$:{:.2f}\n O salario com aumento: R$:{:.2f}' .format(n2, n1, n1+n2), end='\n\n\n')
