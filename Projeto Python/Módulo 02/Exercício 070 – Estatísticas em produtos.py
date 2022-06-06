# 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

from os import system

system('cls')

total = caro = menorvalor = quantidade = 0
pbarato = str()

while True:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: R$:'))
    total += valor
    quantidade += 1
    if valor > 1000:
        caro += 1
    if quantidade == 1 or menorvalor >= valor:
        pbarato = produto
        menorvalor = valor
    sair = ' '
    while sair not in 'SN':
        sair = input('Deseja cadastrar um novo produto? [S/N]: ').strip().upper()[0]
    if sair == 'N':
        break

    print()

print(f'\n{quantidade} produtos, valor final é: R$: {total:.2f}')
print(f'{caro} produtos tem o valor acima de R$: 1000,00')
print(f'O produto mais barato é: {pbarato} e seu valor é: R$: {menorvalor:.2f}\n\n')
