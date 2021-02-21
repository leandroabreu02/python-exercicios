# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))
numero4 = int(input('Quarto número: '))
valores = (numero1, numero2, numero3, numero4)
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
  print(f'O primeiro valor 3 apareceu na posição {valores.index(3)+1}')
else:
  print('Não apareceu números 3')
print('Os números pares foram', end=' ')
if numero1 % 2 == 0:
  print(numero1, end=' ')
if numero2 % 2 == 0:
  print(numero2, end=' ')
if numero3 % 2 == 0:
  print(numero3, end=' ')
if numero4 % 2 == 0:
  print(numero4)  

print('Outra forma: ')
for n in valores:
  if n % 2 == 0:
    print(n, end=' ')
