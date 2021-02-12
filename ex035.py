# Desenvolva um programa que leia o comprimeoto de três retas e diga ao usuário se elas podem ou não formar um triângulo
c1 = float(input('Primeiro comprimento: '))
c2 = float(input('Segundo comprimento: '))
c3 = float(input('Terceiro comprimento: '))

if c1 < c2 + c3:
  if c2 < c1 + c3:
    if c3 < c2 + c1:
      print('Os segmentos PODEM formar um triângulo')
    else:
      print('Os segmentos NÃO podem formar um triângulo')
  else:
    print('Os segmentos NÃO podem formar um triângulo')
else:
  print('Os segmentos NÃO podem formar um triângulo')

# if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
#   print('Os segmentos podem formar um triângulo')
# else:
#   print('Os segmentos não podem formar um triângulo')  