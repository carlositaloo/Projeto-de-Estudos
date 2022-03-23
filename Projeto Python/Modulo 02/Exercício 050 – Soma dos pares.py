# 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

from os import system

system('cls')

r = int()
s = 0
print('Digite 6 números:')
for c in range(0, 6):
	n1 = int(input(': '))
	if n1 % 2 == 0:
		r += n1
		s += 1
print(f'\nVocê digitou {s} valores pares\nResultado da soma dos pares: {r}\n')