# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))
numero4 = int(input('Quarto número: '))
numero5 = int(input('Quinto número: '))
numero6 = int(input('Sexto número: '))
soma = 0
for c in [numero1, numero2, numero3, numero4, numero5, numero6]:
  if c % 2 == 0:
    soma += c
print('A soma dos números pares é: {}'.format(soma))