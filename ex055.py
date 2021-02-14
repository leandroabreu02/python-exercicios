# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
peso1 = float(input('1. Qual seu peso? '))
peso2 = float(input('2. Qual seu peso? '))
peso3 = float(input('3. Qual seu peso? '))
peso4 = float(input('4. Qual seu peso? '))
peso5 = float(input('5. Qual seu peso? '))
pesos = [peso1, peso2, peso3, peso4, peso5]
maior_peso = max(pesos)
menor_peso = min(pesos)
print('O maior peso foi: {} kg'.format(maior_peso))
print('O menor peso foi: {} kg'.format(menor_peso))