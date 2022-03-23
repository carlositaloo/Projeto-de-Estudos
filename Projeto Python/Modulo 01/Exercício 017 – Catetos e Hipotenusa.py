# 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
from os import system

system('cls')

print('Com exemplo abaixo enforme os numeros: \n')
print('     │                                     ')
print('  A) │               A ➔ Cateto oposto    ')
print('     │________       B ➔ Cateto adjacente ')
print('         B)                                ')
n1 = float(input('\nColoque o valor de A: '))
n2 = float(input('Coloque o valor de B: '))
s = math.hypot(n1, n2)

'''
s = float
n1 = n1 ** 2
n2 = n2 ** 2
s = n1 + n2

s = s ** (1/2)
# s = math.sqrt(s)
'''

print('\nO valor da Hipotenusa é: {:.2f}\n\n' .format(s))