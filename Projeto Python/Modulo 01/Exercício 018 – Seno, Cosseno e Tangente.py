# 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from os import system
from math import sin, cos, tan, radians

system('cls')

x = float(input('Informe o ângulo qualquer para descobrir o seno, cosseno e tangente: '))

print('\n   O ângulo: {:.1f}°' .format(x))
print('\n     O Seno: {:.2f}' .format(sin(radians(x))))
print('  O Cosseno: {:.2f}' .format(cos(radians(x))))
print(' A tangente: {:.2f}' .format(tan(radians(x))), end='\n\n\n')

# print(' O Seno:{:.2f}\n O Cosseno: {:.2f}\n A Tangente: {:.2f}\n\n' .format(sin(radians(x)), cos(radians(x)), tan(radians(x))))
