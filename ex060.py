# Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex 5! = 5 * 4 * * 3 * 2 * 1 = 120
valor = int(input('Digite um valor: ')) + 1
original = valor - 1
multiplicacao = 1
print('Calculando {}! ='.format(original), end=' ')

varr = 0
while valor != 1:
  valor -= 1
  multiplicacao *= valor
  varr = '{} x'.format(valor)
  print(varr, end=' ')



# dá para tratar a variável valores para tirar o x no final???????
print('= {}'.format(multiplicacao))