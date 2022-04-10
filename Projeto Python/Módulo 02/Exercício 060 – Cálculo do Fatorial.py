# 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from os import system

system('cls')

n1 = int(input('Digite um número para saber seu fatorial: '))
c = n1 - 1
res = n1

print(f'{n1}! = {n1} ', end='')
while c != 0:
    print(f'x {c} ', end='')
    res = res * c
    c -= 1
print(f'= {res}')


# # -------------------------- Usando o for:


# n1 = int(input('Digite um número para saber seu fatorial: '))
# res = 1

# print(f'{n1}! = ', end='')
# for c in range(n1, 0, -1):
#     if c > 1:
#         print(f'{c} x ', end='')
#     else:
#         print(f'{c} = ', end='')
#     res = res * c
# print(res)