# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra a
# em que posição ela aparece pela primeira vez
# em que posição ela aparece a última vez
frase = str(input('Escreva uma frase: ')).upper().strip()
numero_a = frase.count('A')
primeiro_a = frase.find('A')+1
ultimo_a = frase.rfind('A')+1
print('A letra A aparece {} veses na frase'.format(numero_a))
print('O primeiro A aparece na posição {}'.format(primeiro_a))
print('O último A aparece na posição {}'.format(ultimo_a))
