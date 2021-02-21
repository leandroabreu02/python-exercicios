# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))
numero4 = int(input('Quarto número: '))
numero5 = int(input('Quinto número: '))
valores = [numero1, numero2, numero3, numero4, numero5]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {valores} nas posições {valores}')
print(f'O menor valor digitado foi {valores} nas posições {valores}')
