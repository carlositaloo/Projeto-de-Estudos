from os import system

system('cls')

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
p -= r

while c < 10:
    print(f'{p + r} ➜  ', end='')
    p += r
    c += 1