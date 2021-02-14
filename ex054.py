# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
maior_idade = 0
menor_idade = 0
ano_atual = date.today().year
for c in range(0, 7):
  nascimento = int(input('Digite aqui seu ano de nascimento: '))
  idade = ano_atual - nascimento
  if idade >= 18:
    maior_idade += 1
  if idade < 18:
    menor_idade += 1
print('Há {} pessoas maiores de idade e {} menores de idade'.format(maior_idade, menor_idade))
