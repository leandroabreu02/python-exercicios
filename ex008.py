# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = int(input('Valor em metros: '))
centimetros = valor * 100
milimetros = valor * 1000
print('O valor {} corresponde a {} centímetros e {} milímetros'.format(valor, centimetros, milimetros))