from os import system
from random import randint
from rich import print

system('cls')

sair = False
while sair == False:
    bot = randint(0, 10)
    impar = input('\nImpa ou Par? [I/P]: ').strip().upper()[0]
    player = int(input('Digite o número: '))
    print(f'Computador jogou: {bot}')
    res = (bot + player) % 2
    if res == 1 and impar == 'I':
        print('[green][IMPA] Você ganhou, jogo novamente!')
    elif res == 1 and impar == 'P':
        print('[red][IMPA] Voce perdeu, game over')
        sair = True
    elif res == 0 and impar == 'I':
        print('[red][PAR] Voce perdeu, game over')
        break
    elif res == 0 and impar == 'P':
        print('[green][PAR] Você ganhou, jogo novamente!')
    else:
        print('ERRO!!!')
print('\n\n')