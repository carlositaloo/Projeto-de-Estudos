from os import system

system('cls')

close = False
sair = 'xy'
total = caro = menorvalor = quantidade = 0
pbarato = str()


while close == False:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: R$:'))
    total += valor
    quantidade += 1
    if quantidade == 1:
        menorvalor = valor
    if valor > 1000:
        caro += 1
    if menorvalor >= valor:
        pbarato = produto
        menorvalor = valor
    while sair not in 'SN':
        sair = input('Deseja cadastrar um novo produto? [S/N]: ').strip().upper()[0]
        if sair == 'S':
            close = False
        elif sair == 'N':
            close = True
    sair = 'xy'
    print()

print(f'{quantidade} produtos, valor final é: R$: {total:.2f}')
print(f'{caro} produtos tem o valor acima de R$: 1000,00')
print(f'O produto mais barato é: {pbarato} e seu valor é: R$: {menorvalor:.2f}')
