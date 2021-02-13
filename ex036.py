# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai pertuntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você pagará? '))

limite = salario_comprador * 0.3

meses = anos * 12

prestacao = valor_casa / meses

if prestacao > limite:
  print('Empréstimo negado, a prestação seria de R${:.2f}'.format(prestacao))
else:
  print('Empréstimo concedido, a prestação seria de R${:.2f}'.format(prestacao))