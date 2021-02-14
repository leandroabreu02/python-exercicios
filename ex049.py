# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for
numero = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 10+1):
  print('{} * {} = {}'.format(numero, c, numero * c))
print('-' * 12)