# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre
# - a média de idade do grupo
# - qual o nome do homem mais velho
# - quantas mulheres tem menos de 20 anos
nome1 = str(input('Qual seu nome? '))
idade1 = int(input('Qual sua idade? '))
sexo1 = str(input('Qual seu gênero? (m/f) ')).lower()

nome2 = str(input('Qual seu nome? '))
idade2 = int(input('Qual sua idade? '))
sexo2 = str(input('Qual seu gênero? (m/f) ')).lower()

nome3 = str(input('Qual seu nome? '))
idade3 = int(input('Qual sua idade? '))
sexo3 = str(input('Qual seu gênero? (m/f) ')).lower()

nome4 = str(input('Qual seu nome? '))
idade4 = int(input('Qual sua idade? '))
sexo4 = str(input('Qual seu gênero? (m/f) ')).lower()

print('A média de idade do grupo é {} anos'.format((idade1 + idade2 + idade3 + idade4) / 4))