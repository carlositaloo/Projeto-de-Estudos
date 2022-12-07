from os import system
from random import randint

system('cls')

lista = [(int(input('Digite 1 número: ')))]
print('Esse numero foi adicionado ao final da lista')

for c in range(0, 4):
    v = int(input('Digite 1 número: '))

    for c in range(0, 4):
        if v <= lista[c]:
            lista.insert(c, v)
            print(f'O número foi adicionado na {c}ª posição')
            break
        if v >= max(lista):
            lista.append(v)
            print('O numero foi adicionado no FINAL')
            break

print(f'\n{lista}\n\n')
