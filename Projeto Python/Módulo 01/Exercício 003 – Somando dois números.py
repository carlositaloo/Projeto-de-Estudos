# 003: Crie um programa que leia dois números e mostre a soma entre eles.

import os
def clear(): return os.system('cls')


clear()

print('Some dois números:\n')
n1 = int(input(': '))
n2 = int(input(': '))
s = n1 + n2
print('A soma de: {} + {} = {}.\n' .format(n1, n2, s))
