# Crie um programa que faça o computador jogar Jokempô ou pedra, papel e tesoura com você
import random
jogador = str(input('Você vai escolher Pedra, Papel ou Tesoura? ')).lower()
possibilidades = ['pedra', 'papel', 'tesoura']
pc = random.choice(possibilidades)
if jogador == 'pedra' and pc == 'tesoura':
  print('Você venceu!, eu escolhi {} e você escolheu {}'.format(pc, jogador))
elif jogador == 'papel' and pc == 'pedra':
  print('Você venceu!, eu escolhi {} e você escolheu {}'.format(pc, jogador))
elif jogador == 'tesoura' and pc == 'papel':
  print('Você venceu!, eu escolhi {} e você escolheu {}'.format(pc, jogador))
elif jogador == 'pedra' and pc == 'pedra' or jogador == 'papel' and pc == 'papel' or jogador == 'tesoura' and pc == 'tesoura':
  print('Empatou!, eu escolhi {} e você também escolheu {}'.format(pc, jogador))
else:
  print('Eu venci!, eu escolhi {} e você escolheu {}'.format(pc, jogador))