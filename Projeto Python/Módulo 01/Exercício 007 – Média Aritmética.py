# 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# https://youtu.be/Vw6gLypRKmY

# Ordem de Precedência
# 1º ()
# 2º **
# 3º *, /, //, %
# 4º +, -

import os
def clear(): return os.system('cls')


clear()

print('Digite 2 notas para saber a media: ')
n1 = float(input(': '))
n2 = float(input(': '))
print('A média é: {:.1f}' .format((n1+n2)/2), end='\n\n\n')
