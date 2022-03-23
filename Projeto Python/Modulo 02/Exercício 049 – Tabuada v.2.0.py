# 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

from os import system

system('cls')

n1 = int(input('Digite um numero para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{n1} x {c:2} = {n1 * c}')