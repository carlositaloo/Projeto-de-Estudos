from os import system

system('cls')

c = True
quantidade = 0
media = 0
maior = 1000
menor = 1000
while c == True:
    n1 = int(input('Digite um numero: '))
    media += n1
    if quantidade == 0:
        maior = n1
        menor = n1
    else:
        if n1 <= menor:
            menor = n1
        if n1 >= maior:
            maior = n1
    quantidade += 1
    sair = input('Deseja digitar mais numeros [S/N]: ')
    if sair == 'N':
        c = False
print(f'\nVocê digitou {quantidade} números')
print(f'A média de todos valores é: {media / quantidade:.2f}')
print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}\n\n')