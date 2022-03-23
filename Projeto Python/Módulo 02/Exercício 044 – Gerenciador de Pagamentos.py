# 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

from os import system

system('cls')

preço = float(input('Digite o valor a pagar: '))
pagamento = int(input('Forma de pagamento:\n	1.Dinheiro    2.Cartão\nOpção: '))

if pagamento == 1:
    valor = preço * 10 / 100
    print(f'O valor é: R$:{preço} com desconto fica: R$:{preço - valor:.2f}\n(10% de desconto)')
elif pagamento == 2:
    pagamento = int(input('Digite o numero de parcelas: '))
    if pagamento == 1:
        valor = preço * 5 / 100
        print(f'O valor é: R$:{preço:.2f} com desconto fica: R$:{preço - valor:.2f}\n(5% de desconto)')
    elif pagamento == 2:
        print(f'O valor é: R$:{preço:.2f} (Sem desconto)\nA parcela fica: R$:{preço / pagamento:.2f} em {pagamento:.0f}x')
    elif pagamento >= 3:
        valor = preço * 20 / 100
        print(f'O valor é: R$:{preço:.2f} com juros fica: R$:{preço + valor:.2f}\n(20% de juros)\nA parcela fica: R$:{(preço + valor) / pagamento:.2f} em {pagamento:.0f}x')
    else:
        print('ERRO!')
else:
    print('ERRO!')
print('\n')