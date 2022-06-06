from os import system

system('cls')

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))

list = [n1, n2, n3, n4]
tupla = (list)
pares = 0

print(f'\n{tupla}\n')

print(f'A tupla tem {tupla.count(9)} numeros 9.')

if 3 in tupla:
    print(f'A tupla tem o valor 3 na posição: {tupla.index(3)+1}ª')
else:
    print('A tupla não tem o numero 3.')

for c in range(0, 4):
    if tupla[c] % 2 == 0:
        pares += 1

print(f'Os valores pares digitado foram: {pares}\n\n')
