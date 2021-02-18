# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
# No final, mostre
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos
while True:
  print('-' *20)
  print('CADASTRE UMA PESSOA')
  print('-' *20)
  idade = int(input('Idade: '))
  sx = str(input('Sexo: [m/f]').lower()).strip()
  quer_continuar = str(input('Quer continuar? [s/n]')).lower().strip()
  numero_homens = 0
  numero_mulheres = 0

  if quer_continuar == 's':
    numero_homens += 1
    numero_mulheres += 1
  if quer_continuar == 'n':
    print('FIM DO PROGRAMA')
    print(f'Total de pessoas com mais de 18 anos: {maiores_idade}')
    print(f'Ao todo temos {numero_homens} homens cadastrados')
    print(f'E temos {numero_mulheres} mulheres com menos de 20 anos')
    break