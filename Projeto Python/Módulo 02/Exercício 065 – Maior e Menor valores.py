# 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from os import system

system('cls')

c = True
quantidade = media = maior = menor = 0
while c == True:
    n1 = int(input('Digite um numero: '))
    media += n1
    if quantidade == 0:
        maior = n1
        menor = n1
    else:
        if n1 < menor:
            menor = n1
        if n1 > maior:
            maior = n1
    quantidade += 1
    sair = input('Deseja digitar mais numeros [S/N]: ').upper().strip()[0]
    if sair == 'N':
        c = False
print(f'\nVocê digitou {quantidade} números')
print(f'A média de todos valores é: {media / quantidade:.1f}')
print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}\n\n')