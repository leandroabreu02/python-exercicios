# lanche = ('Hambúrguer', 'Pizza', 'Suco', 'Pudim', 'Batata frita')

# for comida in lanche:
#   print(f'Eu vou comer {comida}')

# print('-='*30)

# for cont in range(0, len(lanche)):
#   print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# print('-='*30)

# for pos, comida in enumerate(lanche):
#   print(f'Eu vou comer {comida} na posição {pos}')

# print('Comi pra caramba!')

# -----------------------------------------------------------------
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

# -----------------------------------------------------------------
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
  print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# -----------------------------------------------------------------
# names = ["Sam", "Peter", "James", "Julian", "Ann"]
# print(*names, sep=", ")