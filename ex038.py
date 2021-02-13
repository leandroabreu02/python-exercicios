# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maiorn, os dois são iguais
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
if numero1 > numero2:
  print('O primeiro valor é maior')
elif numero2 > numero1:
  print('O segundo valor é maior') 
else:
  print('Valores iguais') 
  