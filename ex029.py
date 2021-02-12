# Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado  
# a multa vai custar R$7,00 por cada km acima do limite
velocidade = int(input('Qual a velocidade? '))
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print('Você foi multado! Valor da multa R${:.2f}'.format(multa))
else:
  print('Você está dirigindo em segurança! ')