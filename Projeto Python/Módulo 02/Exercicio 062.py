from os import system

system('cls')

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
quit = 1
res = p

while c < 10:
    print(f'{res} ➜  ', end='')
    res += r
    c += 1

while quit > 0:
    quit = int(input('\nQuer ver mais quantas quantia da mesma PA: '))
    
    c -= quit
    res = p
    if quit > 0:
        system('cls')
        while c < 10:
            print(f'{res} ➜  ', end='')
            res += r
            c += 1
