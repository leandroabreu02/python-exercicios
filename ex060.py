# Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex 5! = 5 * 4 * 3 * 2 * 1 = 120



valor = int(input('Digite um valor: ')) + 1                     # USO DO LAÇO WHILE
original = valor - 1
multiplicacao = 1
print('Calculando {}! ='.format(original), end=' ')

varr = 0
while valor != 1:
  valor -= 1
  multiplicacao *= valor
  varr = '{}'.format(valor)
  print(varr, end=' ')
  print('x' if valor > 1 else '=', end=' ')
print('{}'.format(multiplicacao))


# num = int(input('Digite um valor para ver seu fatorial: '))    # USO DO LAÇO FOR
# mult = 1
# print('Calculando {}! ='.format(num), end=' ')
# for num in range (num, 0, -1):
#   print(num, end=' ')
#   print('x' if num > 1 else '=', end=' ')
#   mult *= num
# print('{}'.format(mult))

