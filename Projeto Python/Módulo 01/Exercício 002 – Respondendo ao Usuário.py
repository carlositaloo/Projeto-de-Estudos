# 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

import os
def clear(): return os.system('cls')


clear()

nome = input('Digite seu nome: ')
print('Prazer em te conhecer, {}!\n' .format(nome))
