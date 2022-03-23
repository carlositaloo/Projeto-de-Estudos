# 042: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

from os import system

system('cls')

n1 = input('Digite três retas com - para ver se forma um triangulo:\n> ')
n2 = input('> ')
n3 = input('> ')

n1 = n1.count('-')          # Não necessariamente precisa disso!
n2 = n2.count('-')
n3 = n3.count('-')

if n1 > n2+n3 or n2 > n1+n3 or n3 > n1+n2:
    print('\nNão e possível formar um triangulo')

elif n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('\n')
    if n1 == n2 == n3:
        print('Seu triangulo é:\n Equilátero: todos os lados iguais')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('Seu triangulo é:\n Isósceles: dois lados iguais')
    elif n1 != n2 != n3 != n1:
        print('Seu triangulo é:\n Escaleno: todos os lados diferentes')
else:
    print('ERRO!')
print('\n')
