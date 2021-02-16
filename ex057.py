# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto
s = ''
while s != 'M' and s != 'F':  
  s = input('Qual seu gênero? [M/F] ').strip().upper()[0]

if s == 'M':
  print('Sexo masculino registrado com sucesso')
if s == 'F':
  print('Sexo feminino registrado com sucesso')



# sx = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
# while sx not in 'MmFf':
#   sx = str(input('Dados inválidos, tente novamente: ')).strip().upper()[0]
# print('Sexo {} registrado com sucesso '.format(sx))
