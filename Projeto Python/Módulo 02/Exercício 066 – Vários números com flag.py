# 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

from os import system

system('cls')

total = valores = 0

while True:
    n1 = int(input('Digite um némero para soma-lo, 999 para: '))
    if n1 == 999:
        break
    else:
        total += n1
        valores += 1
print(f'\nVocê digitou {valores} números e a soma deles é: {total}\n\n')