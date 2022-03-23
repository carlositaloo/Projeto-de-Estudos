# 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

import os
clear = lambda: os.system('cls')
clear()

C = float(input('Digite Uma temperatura em graus Celsius para converter a Fahrenheit: '))
F = C * 1.8 + 32

print('Em Celsius:      {}°C' .format(C))
print('Em Fahrenheit:   {}°F' .format(F), end='\n\n\n')