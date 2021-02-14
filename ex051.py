# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
primeiro_termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
# An = A(1) + (n-1) * r       A10 = A(1) + 9*r
for c in range(primeiro_termo, primeiro_termo + 10 * razao, razao):
  print('{}'.format(c), end=' ')