# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Qual seu nome completo? ')).strip()
silva_minusculo = nome.lower()
tem_silva = 'silva' in silva_minusculo
print('Tem Silva no seu nome? {}'.format(tem_silva)) 