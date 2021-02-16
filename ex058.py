# Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 a 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
import random
from time import sleep

numero_pc = ''
numero_escolhido = ' '

palpites = 0

numeros = [0, 1, 2, 3, 4, 5]
numero_pc = random.choice(numeros)


while numero_pc != numero_escolhido:
  
  numero_escolhido = int(input('Qual número de 0 a 10 você acha que o computador pensou? '))
  palpites += 1
  print('PROCESSANDO...')
  sleep(3)
  if numero_pc == numero_escolhido:
    print('Você acertou! Seu número escolhido foi {} e o pc escolheu {}, você precisou de {} palpites para vencer'.format(numero_escolhido, numero_pc, palpites))
  else:
    print('Você errou! Seu número escolhido foi {} e o não escolheu esse'.format(numero_escolhido))



# from random import randint
# computador = randint(0, 10)
# print('Digite um número de 0 a 10 e veja se foi o que eu pensei: ')
# print('Duvido você advinhar qual foi.. ')
# acertou = False
# tentativas = 0
# while not acertou:
#   jogador = int(input('Qual seu palpite? '))
#   tentativas += 1
#   if jogador == computador:
#     acertou = True
#   else:
#     if jogador < computador:
#       print('Mais.. Tente novamente')
#     elif jogador > computador:
#       print('Menos.. Tente novamente')
# print('Acertou com {} tentativas. Parabens!'.format(tentativas))
