# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
valor = float(input('Qual o valor a ser pago? R$'))
print('''Forma de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
if opcao == 1:
  print('À vista no dinheiro ou cheque, com 10% de desconto, sai por R${:.2f}'.format(valor * 0.9))
elif opcao == 2:
  print('À vista no cartão, com 5% de desconto, sai por R${:.2f}'.format(valor * 0.95))
elif opcao == 3:
  print('Em até 2x no cartão, sai pelo preço normal de R${:.2f}, custando RS${:.2f} cada parcela'.format(valor, valor/ 2))
else:
  parcelas = int(input('Quantas parcelas? '))
  print('3x ou mais no cartão, com 20% de juros, sai por R${:.2f}, custando R${:.2f} cada parcela'.format(valor * 1.2, valor * 1.2 / parcelas))
