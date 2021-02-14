# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
# 2 3 5 7 11 13 17 19 23
numero = int(input('Digite um número e veja se ele é primo ou não: '))
total = 0
for c in range (1, numero + 1):
  if numero % c == 0:
    print('\033[33m', end='')
    total += 1
  else:
    print('\033[31m', end='')
  print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
  print('O número é primo')
else:
  print('O número não é primo')