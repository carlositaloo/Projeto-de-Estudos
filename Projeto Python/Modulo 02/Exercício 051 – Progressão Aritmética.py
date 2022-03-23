# 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

from os import system

system('cls')

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão da PA: '))
q = 9 * r + p
for c in range(p, q+1, r):
    print(c, end=' ➜  ')
