# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas
distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
  preco = distancia * 0.5
  print('A viagem vai custar R${:.2f}'.format(preco))
else:
  preco = distancia * 0.45
  print('A viagem vai custar R${:.2f}'.format(preco)) 