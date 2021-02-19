# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
# No final, mostre
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos
numero_homens = 0
maiores_idade = 0
numero_mulheres_20 = 0

while True:
  print('-' *20)
  print('CADASTRE UMA PESSOA')
  print('-' *20)
  idade = int(input('Idade: '))
  sx = str(input('Sexo: [M/F]')).strip().lower()[0]
  quer_continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]

  if sx == 'm':
    numero_homens += 1
  if idade > 18:
    maiores_idade += 1
  if idade <=20 and sx == 'f':
    numero_mulheres_20 += 1
    
  if quer_continuar == 'n':
    print('FIM DO PROGRAMA')
    print(f'Total de pessoas com mais de 18 anos: {maiores_idade}')
    print(f'Ao todo temos {numero_homens} homens cadastrados')
    print(f'E temos {numero_mulheres_20} mulheres com menos de 20 anos')
    break
