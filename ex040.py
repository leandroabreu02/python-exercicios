# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida
# - média abaixo de 5.0, reprovado
# - média entre 5.0 e 6.9, recuperação
# - média 7.0 ou superior, aprovado
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
  print('Sua média foi {}, você foi reprovado'.format(media))
elif 5.0 <= media < 6.9:
  print('Sua média foi {}, você vai ficar de recuperação'.format(media))
else:
  print('Sua média foi {}, parabéns, você foi aprovado! '.format(media))