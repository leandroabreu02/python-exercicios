lanche = ('Hambúrguer', 'Pizza', 'Suco', 'Pudim', 'Batata frita')

for comida in lanche:
  print(f'Eu vou comer {comida}')

print('-='*30)

for cont in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-='*30)

for pos, comida in enumerate(lanche):
  print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
