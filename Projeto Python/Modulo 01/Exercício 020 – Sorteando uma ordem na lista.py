# 020: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from os import system
import random

system('cls')

print('Digite o nome de 4 alunos para sortear a ordem de trabalho:')
a1 = input('1 : ')
a2 = input('2 : ')
a3 = input('3 : ')
a4 = input('4 : ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('\nA ordem de alunos escolhido foi: \n{}\n\n' .format(lista))