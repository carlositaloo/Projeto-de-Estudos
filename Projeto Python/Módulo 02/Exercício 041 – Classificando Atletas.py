# 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from os import system
from datetime import date

system('cls')

date = date.today().year
id = int(input('Digite a data de nascimento do atleta: '))
id = date - id
print(f'o atleta tem: {id} anos')

if 0 < id < 10:
    print('Atleta: MIRIM')
elif 0 < id < 15:
    print('Atleta: INFANTIL')
elif 0 < id < 20:
    print('Atleta: JUNIOR')
elif 0 < id < 26:
    print('Atleta: SÊNIOR')
elif 0 < id > 25:
    print('Atleta: MASTER')
else:
    print('ERRO!')
