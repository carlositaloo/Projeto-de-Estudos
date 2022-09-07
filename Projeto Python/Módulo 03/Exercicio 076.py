from os import system

system('cls')

tupla = ('Notebook', 7500,
         'Tablet', 3000,
         'Mouse', 450,
         'Teclado', 700,
         'Headset', 350,
         'Internet', 70)

for c in range(0, len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:.<20}', end='')
    else:
        print(f'R$:{tupla[c]:>8.2f}')