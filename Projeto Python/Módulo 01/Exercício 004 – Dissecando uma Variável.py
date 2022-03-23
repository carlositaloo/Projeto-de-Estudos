# 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

import os
def clear(): return os.system('cls')


clear()

y = input('\nDigite algo: ')
print('O tipo primitivo desse valor é ', type(y))
print('\n So contem espaço? ', y.isspace())
# apenas espaço
print(' É um numero? ', y.isnumeric())
# apenas numeros
print(' E alfabético? ', y.isalpha())
# apenas letras
print(' É alfanumerico? ', y.isalnum())
# letras e numeros
print(' Está capitalizada? ', y.istitle())
# maiúscula e minúscula
print(' Está em maisculas? ', y.isupper())
# apenas maiúsculas
print(' Está em minusculas? {}\n\n' .format(y.islower()))
# apenas minúsculas
