# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - se ele ainda vai se alistar no serviço militar
# - se é a hora de se alistar
# - se já passou o tempo de alistamento
# seu programa também deverá o tempo que falta ou o tempo que já passou do prazo
from datetime import date
ano_atual = date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = ano_atual - nascimento
if nascimento > ano_atual:
  print('Você veio do futuro? Nasceu no ano de {}'.format(nascimento))
elif nascimento < ano_atual:
  print('Qual seu gênero?:\n[ 1 ] para MASCULINO\n[ 2 ] para FEMININO')
  genero = int(input('Sua opção: '))
  if genero == 2:
    print('Você não precisa se alistar')
  elif genero == 1:
    if idade < 18:
      anos = 18 - idade
      print('Você tem {} anos e ainda vai se alistar para o exército, falta {} anos'.format(idade, anos))
      print('Você vai se alistar no ano de {}'.format(nascimento + 18))
    elif idade == 18:
      print('Você tem {} anos, é hora de se alistar '.format(idade))
    elif idade > 18:
      anos = idade - 18
      print('Você tem {} anos, já passou seu tempo de alistamento em {} anos'.format(idade, anos))
      print('Você deveria ter se alistado no ano de {}'.format(nascimento + 18))
  elif genero != 2 and genero != 1:
    print('Coloque 1 ou 2 para saber o seu gênero')
    print('Reinicie o programa')
