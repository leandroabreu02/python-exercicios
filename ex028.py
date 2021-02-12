# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computadpr
# o programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep
numeros = [0, 1, 2, 3, 4, 5]
numero_pc = random.choice(numeros)
numero_escolhido = int(input('Qual número você acha que o computador pensou? '))
print('PROCESSANDO...')
sleep(3)
if numero_pc == numero_escolhido:
  print('Você acertou! Seu número escolhido foi {} e o pc escolheu {}'.format(numero_escolhido, numero_pc))
else:
  print('Você errou! Seu número escolhido foi {} e o pc escolheu {}'.format(numero_escolhido, numero_pc))
