# 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

from os import system


sair = ''
while sair == '':
    system('cls')
    n1 = float(input('Digite o valor de 2 notas:\n> '))
    n2 = float(input('> '))

    media = float((n1 + n2) / 2)
    print(f'Média: {media:.1f}\n\n')

    if 0 < media < 5:
        print('REPROVADO!\n\n')
    elif 7 > media >= 5:
        print('RECUPERAÇÃO!\n\n')
    elif media >= 7 and media <= 10:
        print('APROVADO!\n\n')
    else:
        print('ERRO!\n\n')
    sair = input('Pressione Enter para rodar de novo')
