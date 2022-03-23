# 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from os import system
from rich import print

system('cls')

n1 = int(input('Digite a sua velocidade atual: '))


if n1 > 80:
    n2 = float((n1 - 80) * 7.00)
    print(f'Você foi multado em R$:{n2:.2f}')
else:
    print('Sua velocidade é ideal, nao ultrapasse 80km')
print('\n\n\n')
