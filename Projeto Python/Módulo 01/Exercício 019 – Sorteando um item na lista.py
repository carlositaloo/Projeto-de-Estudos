# 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from os import system
import random

system('cls')

print('Digite o nome de 4 alunos:')
a1 = input('1° : ')
a2 = input('2° : ')
a3 = input('3° : ')
a4 = input('4° : ')
list = [a1, a2, a3, a4]
n1 = random.choice(list)

print('\nO aluno escolhido foi: {}' .format(n1), end='\n\n\n')

'''
n1 = random.randint(1, 4)
print('\nO aluno escolhido foi:')
if n1 == 1:
    print('1 - {}' .format(a1))
elif n1 == 2:
    print('2 - {}' .format(a2))
elif n1 == 3:
    print('3 - {}' .format(a3))
elif n1 == 4:
    print('4 - {}\n\n' .format(a4))
'''