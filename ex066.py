# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)
n = 0
soma = 0
quantidade = 0
while True:
  n = int(input('Digite um valor [999 para parar]: '))
  if n != 999:
    soma += n
    quantidade += 1
  if n == 999:
    break
print(f'Foram digitados {quantidade} números e a soma entre eles é {soma}')