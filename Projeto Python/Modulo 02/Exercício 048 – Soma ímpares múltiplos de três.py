# 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

from os import system

system('cls')

r = 0
s = int()
for c in range(1, 501, 2):      
    if c % 3 == 0:
        print(c, end=' ')
        r += c
        s += 1
print(f'\n\nsoma dos {s} numero deu:\nReseultado: {r}\n')
