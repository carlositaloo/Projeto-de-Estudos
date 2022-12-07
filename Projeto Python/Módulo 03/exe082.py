from os import system
from random import randint

system('cls')

lista0 = []
lista1 = []
lista2 = []

while True:
    radomize = input('Deseja randomizar sozinhos os números? [S/N]: ').upper()
    if radomize == 'S':
        random = randint(5, 10)
        for c in range(random):
            lista0.append(randint(0, 10))
        break
    if radomize == 'N':
        random = int(input('Quantos números ira por: '))
        for c in range(random):
            lista0.append(int(input('Digite um numero: ')))
        break

for p, v in enumerate(lista0):
    if lista0[p] % 2 == 0:
        lista1.append(v)
    else:
        lista2.append(v)

print(f'A lista completa é: {lista0}')
print(f'A lista de pares é: {lista1}')
print(f'A lista de impares: {lista2}\n\n')