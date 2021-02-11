# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real = float(input('Digite um valor de dinheiro em real: '))
dolar = real / 5.39
print('Você tem {:.2f} dólares'.format(dolar))