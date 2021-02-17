# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag - 999)
n = 0
soma = 0
quantidade = 0
n = int(input('Digite um valor: '))
while n != 999:
  soma += n
  quantidade += 1
  n = int(input('Digite um valor: '))
print('Foram digitados {} valores e a soma entre eles é igual a {}'.format(quantidade, soma))
