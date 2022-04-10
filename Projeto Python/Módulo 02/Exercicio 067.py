from os import system

system('cls')

sair = False


while sair == False:
    n1 = int(input('Deseja ver a tabuada de qual valor: '))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1} x {c:2} = {n1*c}')
    print('-='*20)