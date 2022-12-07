from os import system
from random import randint

system('cls')

lista = []

while True:
    radomize = input('Deseja randomizar sozinhos os números? [S/N]: ').upper()
    if radomize == 'S':
        random = randint(3, 10)
        for c in range(random):
            lista.append(randint(0, 10))
        break
    if radomize == 'N':
        quantidade = int(input('Quantos números ira por: '))
        for c in range(quantidade):
            lista.append(int(input('Digite um numero: ')))
        break



print(lista)
print(f'\nA quantidade de itens digitados é: {len(lista)}\n')
print(f'A lista em ordem decrescente:\n{sorted(lista,reverse=True)}\n')

if 5 in lista:
    print('Tem o número 5 na posição: ', end='')
    for p, v in enumerate(lista):
        if 5 == v:
            print (f'{p+1}ª, ', end='')
        
else:
    print('Não a nem um número 5 na lista')
print('\n\n')
