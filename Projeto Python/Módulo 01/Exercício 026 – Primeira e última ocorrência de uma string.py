# 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

from os import system
system('cls')

frase = input('Digite uma Frase: ').strip().lower()

print('Essa frase contem {} letras A' .format(frase.count('a')))
print('A primeira letra esta na posição: {}' .format(frase.find('a')+1))
print('A ultima letra esta na posição: {}' .format(frase.rfind('a')+1), end='\n\n\n')
