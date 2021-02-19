# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre
# a) qual é o total gasto na compra
# b) quantos produtos custam mais de R$ 1000
# c) qual é o nome do produto mais barato
mais_1000 = 0
preco = 0
total_gasto = 0
nome_barato = ''

while True:
  nome_produto = str(input('Qual o nome do produto? ')).strip()
  preco = float(input('Qual o preço do produto? '))
  quer_continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]

  if preco > 1000:
    mais_1000 += 1
  total_gasto += preco
  if preco < preco:                        # rotina para pegar nome do produto mais barato
    nome_barato = nome_produto

  if quer_continuar == 'n':
    print('FIM DO PROGRAMA')
    print(f'No total R${total_gasto:.2f} foram gastos na compra')
    print(f'{mais_1000} produtos custam mais de R$ 1000.00')
    print(f'{nome_barato} é o produto mais barato')