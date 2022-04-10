# 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

from os import system

system('cls')

n1 = q = c = 0

while n1 != 999:
    n1 = int(input('Digite um numero, ou 999 para sair:'))
    if n1 == 999:
        print(f'\n Quantidade de numeros digitados: {q}')
        print(f' Soma dos valores: {c}\n\n')
    else:
        q += 1
        c += n1

