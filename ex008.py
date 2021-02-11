# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = int(input('Valor em metros: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('O valor corresponde a {} km'.format(km))
print('O valor corresponde a {} hm'.format(hm))
print('O valor corresponde a {} dam'.format(dam))
print('O valor corresponde a {} dm'.format(dm))
print('O valor corresponde a {} cm'.format(cm))
print('O valor corresponde a {} mm'.format(mm))