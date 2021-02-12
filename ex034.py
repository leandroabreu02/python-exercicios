# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# para salários superiores a R$1.250,00, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o seu salário: '))
if salario > 1250:
  print('O seu novo salário é: R${:.2f}'.format(salario * 1.1))
else:
  print('O seu novo salário é: R${:.2f}'.format(salario * 1.15))