# 058: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from os import system
from random import randint
system('cls')

bot = randint(0, 10)
voce = -1
# print(bot)

print('BOT: pensei um nemero de 0 a 10: ')
tentativa = 1

while voce != bot:
    voce = int(input('Qual seu palpite: '))
    tentativa += 1
    if bot > voce:
        print('Mais... Você nao acertou tente novamente:')
    elif bot < voce:
        print('Menos... Você nao acertou tente novamente:')
print(f'\nVocê acertou o numero do bot: {bot} na {tentativa}ª tentativa\n')
