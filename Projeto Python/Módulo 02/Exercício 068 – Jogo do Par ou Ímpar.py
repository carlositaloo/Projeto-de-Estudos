# 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from os import system
from random import randint
from rich import print

system('cls')

vitoria = 0
while True:
    impar = ' '
    while impar not in 'IP':
        impar = input('\nImpa ou Par? [I/P]: ').strip().upper()[0]
    player = int(input('Digite o número: '))
    bot = randint(0, 10)
    print(f'Computador jogou: {bot}')
    res = (bot + player) % 2
    if res == 1 and impar == 'I':
        print('[green][IMPA] Você ganhou, jogo novamente!')
        vitoria += 1
    elif res == 1 and impar == 'P':
        print('[red][IMPA] Voce perdeu, game over')
        break
    elif res == 0 and impar == 'I':
        print('[red][PAR] Voce perdeu, game over')
        break
    elif res == 0 and impar == 'P':
        print('[green][PAR] Você ganhou, jogo novamente!')
        vitoria += 1
    else:
        print('ERRO!!!')
print(f'\n[blue]Você teve {vitoria} vitórias consecutivas\n\n')