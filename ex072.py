# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
lista_num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onde', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
  num = int(input('Digite um número entre 0 e 20: '))
  if 0 <= num <= 20:
    print(f'Você digitou o número {lista_num[num]}')
    break
  else:
    while True:
      num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
      if 0 <= num <= 20:
        print(f'Você digitou o número {lista_num[num]}')
        break

# Outra maneira
while True:
  while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
      break
    print('Tente novamente. ', end='')

  print(f'Você digitou o número {lista_num[núm]}')
  continua = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
  if continua == 'n':
    break
  
