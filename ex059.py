# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ]somar
# [ 2 ]multiplicar
# [ 3 ]maior
# [ 4 ]novos números
# [ 5 ]sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
escolha = 4
while escolha == 4:
  vl1 = int(input('Primeiro valor: '))
  vl2 = int(input('Segundo valor: '))
  escolha = int(input('''
  O que você quer fazer?
  [ 1 ] somar
  [ 2 ] multiplicar
  [ 3 ] maior
  [ 4 ] novos números
  [ 5 ] sair do programa

  '''))

  if escolha == 1:
    print(vl1 + vl2)
  elif escolha == 2:
    print(vl1 * vl2)
  elif escolha == 3:
    if vl1 > vl2:
      print('Valor 1 maior')
    if vl2 > vl1:
      print('Valor 2 maior')
    else:
      print('Valores iguais')
  elif escolha == 5:
    print('Fim do programa!')
  else:           
    print('Tente novamente')
    escolha = 4 
