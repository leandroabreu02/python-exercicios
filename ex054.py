# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
ano_atual = date.today().year
nasc1 = int(input('1. Qual seu ano de nascimento? '))
nasc2 = int(input('2. Qual seu ano de nascimento? '))
nasc3 = int(input('3. Qual seu ano de nascimento? '))
nasc4 = int(input('4. Qual seu ano de nascimento? '))
nasc5 = int(input('5. Qual seu ano de nascimento? '))
nasc6 = int(input('6. Qual seu ano de nascimento? '))
nasc7 = int(input('7. Qual seu ano de nascimento? '))

idade1 = date.today().year - nasc1
idade2 = date.today().year - nasc2
idade3 = date.today().year - nasc3
idade4 = date.today().year - nasc4
idade5 = date.today().year - nasc5
idade6 = date.today().year - nasc6
idade7 = date.today().year - nasc7

idades = [idade1, idade2, idade3, idade4, idade5, idade6, idade7]

for c in idades:
  if c >= 21:
    print('{} maior de i')
  if c < 21:
    print('{} menor de i')