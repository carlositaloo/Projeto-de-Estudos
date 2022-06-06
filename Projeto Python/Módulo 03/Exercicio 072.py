from os import system

system('cls')

numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

contagem = int(input('Digite um número de 0 a 20 para saber seu nome por extenso: '))

while contagem not in range(0, 21):
    contagem = int(input('Digite um número de 0 a 20 para saber seu nome por extenso: '))
print(f'\n    Voce Digitou: {contagem} - {numero[contagem]}\n\n')
