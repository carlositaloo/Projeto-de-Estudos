# # 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

from os import system

system('cls')

frase = input('Digite uma frase: ').strip()
contrario = frase.replace(' ', '').upper()
if contrario == contrario[::-1]:
    print(f'Sua frase: {frase}\nÉ um Palíndromo')
else:
    print(f'Sua frase: {frase}\nNÃO é um Palíndromo')
