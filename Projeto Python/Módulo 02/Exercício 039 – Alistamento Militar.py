# 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from os import system
from datetime import date

system('cls')

idade = int(input('Digite o ano de seu nascimento: '))
ano = date.today().year

idade = ano - idade

if idade < 18:
    alistamento = 18 - idade
    print(f'\n Voce terá que se alistar no ano de: {ano + alistamento}\n\n')
elif idade == 18:
    print('\n Você tem que se alistar esse ano!\n\n')
elif idade >= 18:
    alistamento = 18 - idade
    print(f'\n Você passou do perido de se alistar, procure uma junta militar!\n O alistamento deveria te sido feito em: {alistamento + ano}\n')
else:
    print('ERRO!')
