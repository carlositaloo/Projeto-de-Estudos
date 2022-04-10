from os import system

system('cls')

c = True
total = valores = 0

while c == True:
    n1 = int(input('Digite um némero para soma-lo, 999 para: '))
    if n1 == 999:
        break
    else:
        total += n1
        valores += 1
print(f'\nVocê digitou {valores} números e a soma deles é: {total}\n\n')