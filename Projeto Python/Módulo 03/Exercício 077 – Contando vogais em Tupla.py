# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

from os import system

system('cls')

palavras = ('Aprender', 'Programador', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Futuro')

for p in palavras:
    print(f'\nNa palavra {p} tem as vogais: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=', ')
