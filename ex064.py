# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag - 999)
n = 0
soma = 0
quantidade = 0
while n != 999:
  n = int(input('Digite um valor: '))
  soma += n
  quantidade += 1
print('Foram digitados {} valores e a soma entre eles é igual a {}'.format(quantidade - 1, soma - 999))
