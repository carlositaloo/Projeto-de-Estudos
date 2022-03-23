# 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

import os
clear = lambda: os.system('cls')
clear()

n1 = float(input('Coloque o comprimento da parede: '))
n2 = float(input('Coloque o tamanho da parede: '))
lt = n1*n2
print('Um litro de tinta pinta 2m², sua parede e do tamanho {}m²\n Logo ira precisar de {} litros de tinta.' .format(lt, lt/2), end='\n\n\n')
