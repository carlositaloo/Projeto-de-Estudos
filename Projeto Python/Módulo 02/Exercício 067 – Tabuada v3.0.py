# 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

from os import system

system('cls')

while True:
    n1 = int(input('Deseja ver a tabuada de qual valor: '))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1} x {c:2} = {n1*c}')
    print('-='*20)