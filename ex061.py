# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
primeiro_termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termo = 0
n = 0
while termo < 10:
  print('{}'.format(primeiro_termo + n * razao), end=' ')
  termo += 1
  n += 1




# primeiro_termo = int(input('Qual o primeiro termo? '))
# razao = int(input('Qual a razão? '))
# # An = A(1) + (n-1) * r       A10 = A(1) + 9*r
# for c in range(primeiro_termo, primeiro_termo + 10 * razao, razao):
#   print('{}'.format(c), end=' ')