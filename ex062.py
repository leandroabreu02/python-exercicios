# Melhore o desafio 061, perguntando para o usuário se ele quer mostra mais alguns termos. O programa encerra quando ele disser que quer mostrar os termos


primeiro_termo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termo = 0
n = 0
while termo < 10:
  print('{}'.format(primeiro_termo + n * razao), end=' ')
  termo += 1
  n += 1
