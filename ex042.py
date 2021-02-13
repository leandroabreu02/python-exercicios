# Refaça o ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - equilátero: todos os lados iguais
# - isósceles: dois lados iguais
# - escaleno: todos os lados diferentes
c1 = float(input('Primeiro comprimento: '))
c2 = float(input('Segundo comprimento: '))
c3 = float(input('Terceiro comprimento: '))

if c1 < c2 + c3:
  if c2 < c1 + c3:
    if c3 < c2 + c1:
      if c1 == c2 == c3:
        print('Os segmentos PODEM formar um triângulo equilátero')
      elif c1 == c2 or c1 == c3 or c2 == c3:
        print('Os segmentos PODEM formar um triângulo isósceles')
      else:
        print('Os segmentos PODEM formar um triângulo escaleno')
    else:
      print('Os segmentos NÃO podem formar um triângulo')
  else:
    print('Os segmentos NÃO podem formar um triângulo')
else:
  print('Os segmentos NÃO podem formar um triângulo')