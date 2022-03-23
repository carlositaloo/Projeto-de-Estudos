# 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

from os import system
from rich import print

system('cls')

n1 = float(input('Digite o valor do seu salario: '))

if n1 > 1250:
    n2 = n1 * 10 / 100
    print(f'Seu salario recebe o aumento de R$:{n2:.2f} e fica R$:{n1 + n2:.2f}')
if n1 <= 1250:
    n2 = n1 * 15 / 100
    print(f'Seu salario recebe o aumento de R$:{n2:.2f} e fica R$:{n1 + n2:.2f}')
