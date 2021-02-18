# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo
n = c = 0 
while True:
  print('-' * 40)
  n = int(input('Digite um número para ver sua tabuada: '))
  print('-' * 40)
  if n > 0:
    for c in range(1, 10+1):
      print(f'{n} * {c} = {n * c}')
    # while n < 11:
    #   print(f'{n} * {c} = {n * c}')
    #   n += 1
  if n < 0:
    break
print('Programa TABUADA encerrado, volte sempre! ')