# 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from os import system
from time import sleep

system('cls')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
    system('cls')
print('BOOM!')