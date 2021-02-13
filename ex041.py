# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# - até 9 anos, mirim
# - até 14 anos, infantil
# - até 19 anos, junior
# - até 25 anos, sênior
# - acima, master
from datetime import date
ano_atual = date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = ano_atual - nascimento
if idade <= 9:
  print('Sua idade de {} anos torna você na categoria mirim'.format(idade))
elif 9 < idade <= 14:
  print('Sua idade de {} anos torna você na categoria infantil'.format(idade))
elif 14 < idade <= 19:
  print('Sua idade de {} anos torna você na categoria junior'.format(idade))
elif 19 < idade <= 25:
  print('Sua idade de {} anos torna você na categoria sênior'.format(idade))
else:
  print('Sua idade de {} anos torna você na categoria master'.format(idade))
