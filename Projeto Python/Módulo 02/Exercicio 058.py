from os import system
from random import randint
system('cls')

bot = randint(0, 10)
# print(bot)

voce = int(input('Digite um nemero de 0 a 10: '))
tentativa = 1

while voce != bot:
    voce = int(input('Você nao acertou tente novamente: '))
    tentativa += 1
print(f'\nVocê acertou o numero do bot: {bot} na {tentativa}ª tentativa\n')
