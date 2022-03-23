# 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import os
import math

clear = lambda: os.system('cls')
clear()

n1 = float(input('Digite um número real: '))


print('\nO numero tem a potencia inteira de: {}' .format(math.trunc(n1)), end='\n\n')

print('O número {} tem a parte inteira de: {:.0f}' .format(n1, n1), end='\n\n')

print('O número {} tem a parte inteira de: {}' .format(n1, int(n1)), end='\n\n\n')
