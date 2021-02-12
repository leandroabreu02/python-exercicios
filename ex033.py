# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
# numero1 = float(input('Primeiro número: '))
# numero2 = float(input('Segundo número: '))
# numero3 = float(input('Terceiro número: '))

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o último número: '))
if numero1 == numero2 and numero1 == numero3 and numero2 == numero3:
    print('Todos os valores são iguais')
else:
    if numero1 >= numero2 and numero1 >= numero3:
        maior = numero1
    if numero2 >= numero1 and numero2 >= numero3:
        maior = numero2
    if numero3 >= numero1 and numero3 >= numero2:
        maior = numero3
    print('O número {} é o maior'.format(maior))
    if numero1 <= numero2 and numero1 <= numero3:
        menor = numero1
    if numero2 <= numero1 and numero2 <= numero3:
        menor = numero2
    if numero3 <= numero1 and numero3 <= numero2:
        menor = numero3
    print('E o número {} é o menor'.format(menor))

# numeros = [numero1, numero2, numero3]
# print('O maior valor digitado foi {}'.format(max(numeros)))
# print('O menor numero digitado foi {}'.format(min(numeros)))

# if numero1 > numero2 > numero3:
#   print('O primeiro número ({}) é o maior e o terceiro ({}) é o menor'.format(numero1, numero3))
# if numero1 > numero3 > numero2:
#   print('O primeiro número ({}) é o maior e o segundo  ({}) é o menor'.format(numero1, numero2))
# if numero2 > numero1 > numero3:
#   print('O segundo número ({}) é o maior e o terceiro ({}) é o menor'.format(numero2, numero3))
# if numero2 > numero3 > numero1:
#   print('O segundo número ({}) é o maior e o primeiro ({}) é o menor'.format(numero2, numero1))
# if numero3 > numero1 > numero2:
#   print('O terceiro número ({}) é o maior e o segundo  ({}) é o menor'.format(numero3, numero2))
# if numero3 > numero2 > numero1:
#   print('O terceiro número ({}) é o maior e o primeiro ({}) é o menor'.format(numero3, numero1))
