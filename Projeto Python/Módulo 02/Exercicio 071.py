from os import system

system('cls')

sacar = int(input('          Valor a sacar R$: '))
cedulas = [200, 100, 50, 20, 10, 5, 1]
c = 0
print('-='*20, end='-\n')

while sacar > 0:
    quantidade = sacar // cedulas[c]
    sacar -= quantidade * cedulas[c]
    if quantidade > 0:
        print(f'{quantidade:2} cédulas de R$: {cedulas[c]:3}'.center(41))
    c += 1
print('-='*20, end='-\n\n')

