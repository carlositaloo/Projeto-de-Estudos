# 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

from os import system
system('cls')

n = int(input('Digite um numero até 4 caracteres: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f"\n{'Unidade:':>8} {u}")
print(f"{'Dezena:':>8} {d}")
print(f"{'Centena:':>8} {c}")
print(f"{'Milhar:':>8} {m}", end='\n\n\n')

# print('\n Unidade: {}' .format(n[3]))
# print('  Dezena: {}' .format(n[2]))
# print(' Centena: {}' .format(n[1]))
# print('  Milhar: {}' .format(n[0]), end='\n\n\n')
