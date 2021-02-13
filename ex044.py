# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
valor = float(input('Qual o valor a ser pago? R$'))
print('À vista no dinheiro ou cheque, com 10% de desconto, sai por R${:.2f}'.format(valor * 0.9))
print('À vista no cartão, com 5% de desconto, sai por R${:.2f}'.format(valor * 0.95))
print('Em até 2x no cartão, sai pelo preço normal de R${:.2f}'.format(valor))
print('3x ou mais no cartão, com 20% de juros, sai por R${:.2f}'.format(valor * 1.2))