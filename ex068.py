# Faça um programa que jogue par ou ímpar.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

# se eu escolhi par, o pc escolhe impar
# se eu escolhi impr, o pc escolhe
import random
possibilidades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_pc = random.choice(possibilidades)         # pc escolheu um par ou impar
soma = 0
numero_vitorias = 0

while True:
  n = int(input('Digite um valor: '))                       # eu digito um valor
  par_ou_impar = str(input('Par ou ímpar? [p/i]')).lower()     # digo se é par ou impar a soma
  soma = n + numero_pc
  print(f'{soma} = {n} + {numero_pc}')
  
  if soma % 2 == 0:
    if par_ou_impar == 'p':
      numero_vitorias += 1
      print(f'Você jogou {n} e o computador {numero_pc}. Total de {soma} DEU PAR')
      print('Você venceu!')
      print('Vamos jogar novamente...')
    else:
      print('Você PERDEU!')
      print(f'GAME OVER, você venceu {numero_vitorias} vezes')
      break
  if soma % 2 == 1:
    if par_ou_impar == 'i':
      numero_vitorias += 1
      print(f'Você jogou {n} e o computador {numero_pc}. Total de {soma} DEU ÍMPAR')
      print('Você venceu!')
      print('Vamos jogar novamente...')
    else:
      print('Você PERDEU!')
      print(f'GAME OVER, você venceu {numero_vitorias} vezes')
      break