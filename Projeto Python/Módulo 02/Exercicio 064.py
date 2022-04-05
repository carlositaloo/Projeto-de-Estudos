from os import system

system('cls')

n1 = 0
q = 0
c = 0

while n1 != 999:
    n1 = int(input('Digite um numero, ou 999 para sair:'))
    if n1 == 999:
        print(f'\n Quantidade de numeros digitados: {q}')
        print(f' Soma dos valores: {c}\n\n')
    else:
        q += 1
        c += n1

