# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre
# a) qual é o total gasto na compra
# b) quantos produtos custam mais de R$ 1000
# c) qual é o nome do produto mais barato
total = 0
totmil = 0
menor = 0
cont = 0
barato = ''
while True:
  produto = str(input('Qual o nome do produto? '))
  preco = float(input('Qual o preço do produto? '))
  cont += 1
  total += preco
  if preco > 1000:
    totmil += 1
  if cont == 1 or preco < menor:
    menor = preco
    barato = produto
  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if resp == 'N':
    break
print('FIM DO PROGRAMA')
print(f'No total R${total:.2f} foram gastos na compra')
print(f'{totmil} produtos custam mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
