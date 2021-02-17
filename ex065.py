# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
n = 0
pergunta = ''
soma = 0
maior = 0
menor = 0
numero_de_perguntas = 0
while pergunta != 'n':
  n = int(input('Digite um valor: '))
  pergunta = input('Quer continuar? [s/n] ').lower()
  numero_de_perguntas += 1
  soma += n
  if numero_de_perguntas == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
print('Você digitou {} números e a média foi {:.2f}'.format(numero_de_perguntas, soma / numero_de_perguntas))
print('O maior valor foi {} e o menor for {}'.format(maior, menor))