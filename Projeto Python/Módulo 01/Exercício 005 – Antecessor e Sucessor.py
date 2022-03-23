# 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

# https://youtu.be/Vw6gLypRKmY

# Ordem de Precedência
# 1º ()
# 2º **
# 3º *, /, //, %
# 4º +, -

import os
def clear(): return os.system('cls')


clear()

n1 = int(input('Digite um numero para saber o antecessor e o proximo: '))
print('{} . {} . {}\n\n' .format(n1-1, n1, n1+1))
