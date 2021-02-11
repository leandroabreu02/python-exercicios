# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto
preco = int(input('Digite o preço atual:R$ '))
desconto = preco * 0.95
print('O preço com o desconto fica R${:.2f}'.format(desconto))