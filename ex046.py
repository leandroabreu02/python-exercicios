# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifíciom, indo de 10 até , com uma pausa de 1 segundo entre eles
from time import sleep
print('Espere a contagem regressiva')
for c in range(10, -1, -1):
  print(c)
  sleep(1)
print('Estouraram!')