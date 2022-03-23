# 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# https://youtu.be/Vw6gLypRKmY

# Ordem de Precedência
# 1º ()
# 2º **
# 3º *, /, //, %
# 4º +, -

import os
def clear(): return os.system('cls')


clear()

n1 = int(input('Digite um numero: '))
print(' Número: {}\n Dobro: {}\n Triplo: {}\n Raiz: {:.2f}' .format(n1, n1+n1, n1*3, n1**(1/2)))
