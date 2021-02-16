# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
n = 0
pergunta = ''
soma = 0
numero_de_perguntas = 0
while pergunta != 'n':
  n = int(input('Digite um valor: '))
  pergunta = input('Quer continuar? [s/n]').lower()
  numero_de_perguntas += 1
  soma += n
print('A média foi {:.2f}'.format(soma / numero_de_perguntas))