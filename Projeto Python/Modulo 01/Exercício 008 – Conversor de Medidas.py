# 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

import os
def clear(): return os.system('cls')


clear()

n1 = float(input('Coloca uma medida em metros para converter em centímetros e milímetros: '))
print('{:0.2f} metros tem: {:.0f} centimetros e {:.0f} milímetros.' .format(n1, n1*100, n1*1000), end='\n\n\n')
